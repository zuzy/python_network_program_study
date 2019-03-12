#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include "cJSON.h"

#define DISABLE "disable"
#define TRAGER  "trager"
#define ON      "on"
#define OFF     "off"

#define MAJOR_PATH  "module/major.rule"
#define INDEP_PATH  "module/indep.conf"
#define SCENE_PATH  "module/scene.conf"
#define DEPEND_PATH "module/depends.conf"
#define STATE_PATH  "module/state.json"

typedef enum {
    NIL = 0,
    EN,
    DIS,
} STATE;

cJSON *parse_from_file(char *path)
{
    char buff[1024] = "";
    char *total = NULL;
    int nread = 0;
    FILE *file = fopen(path, "r");
    if(file) {
        while((nread = fread(buff, 1, 1023, file)) > 0) {
            if(total == NULL) {
                total = strdup(buff);
            } else {
                total = realloc(total, nread + strlen(total) + 1);
                strcat(total, buff);
            }
        }
        fclose(file);
    }
    cJSON *ret = cJSON_Parse(total);
    free(total);
    return ret;
}

cJSON *get_major()
{
    return parse_from_file(MAJOR_PATH);
}

cJSON *get_indep()
{
    return parse_from_file(INDEP_PATH);
}

cJSON *get_scene()
{
    return parse_from_file(SCENE_PATH);
}

cJSON *get_depend()
{
    return parse_from_file(DEPEND_PATH);
}

cJSON *get_state()
{
    return parse_from_file(STATE_PATH);
}

bool check_json_tab(cJSON *tar, char *name)
{
    if(cJSON_GetObjectItem(tar, name)) {
        return true;
    } else {
        return false;
    }
}

bool check_json_list(cJSON *tar, char *name)
{
    bool ret = false;
    int ntar = cJSON_GetArraySize(tar);
    int i;
    for(i = 0; i < ntar; i ++) {
        cJSON *item = cJSON_GetArrayItem(tar, i);
        if(strcmp(item->valuestring, name) == 0) {
            ret = true;
        }
    }
    return ret;
}

bool check_scene(char *action)
{
    cJSON *scene = get_scene();
    bool ret = check_json_tab(scene, action);
    cJSON_Delete(scene);
    return ret;
}

bool check_depend(char *action)
{
    cJSON *depend = get_depend();
    bool ret = check_json_list(depend, action);
    cJSON_Delete(depend);
    return ret;
}

bool check_indep(char *action)
{
    cJSON *indep = get_indep();
    bool ret = check_json_list(indep, action);
    cJSON_Delete(indep);
    return ret;
}

bool check_major(char *action)
{
    cJSON *major = get_major();
    bool ret = check_json_tab(major, action);
    cJSON_Delete(major);
    return ret;
}

bool trager_json_state(cJSON *state, char *action)
{
    cJSON *item = cJSON_GetObjectItem(state, action);
    if(item->type == cJSON_False) {
        return true;
    } else {
        return false;
    }
}

cJSON *set_state(cJSON *state, char *name, STATE action)
{
    switch(action) {
        case NIL: {
            cJSON_ReplaceItemInObject(state, name, cJSON_CreateBool(trager_json_state(state, name)));
            break;
        }
        case EN: {
            cJSON_ReplaceItemInObject(state, name, cJSON_CreateTrue());
            break;
        }
        case DIS: {
            cJSON_ReplaceItemInObject(state, name, cJSON_CreateFalse());
            break;
        }
        default: break;
    } 
    return state;
}

cJSON *delete_item_from(cJSON *array, char *name)
{
    int narray = cJSON_GetArraySize(array);
    int i;
    for(i = 0; i < narray; i++) {
        cJSON *item = cJSON_GetArrayItem(array, i);
        // printf("delete && find %s\n", item->valuestring);
        if(strcmp(item->valuestring, name) == 0) {
            cJSON_DeleteItemFromArray(array, i);
            break;
        }
    }
    return array;
}

cJSON *get_disable_deps(cJSON *state, cJSON *major)
{
    cJSON *deps = get_depend();
    // char *out = cJSON_Print(deps);
    // printf("deps before %s\n", out);
    // free(out);

    int nmajor = cJSON_GetArraySize(major);
    int i;
    for(i = 0; i < nmajor; i++) {
        cJSON *imajor = cJSON_GetArrayItem(major, i);
        cJSON *major_state = cJSON_GetObjectItem(state, imajor->string);
        if(major_state && major_state->type == cJSON_True) {
            // printf("%s is true\n", major_state->string);
            cJSON *mdeps = cJSON_GetObjectItem(imajor, "deps");
            int ndeps = cJSON_GetArraySize(mdeps);
            int j = 0;
            for(j = 0; j < ndeps; j++) {
                cJSON *idep = cJSON_GetArrayItem(mdeps, j);
                // printf("%s %s ", imajor->string, idep->valuestring);
                if(cJSON_GetObjectItem(deps, idep->string)) {
                    delete_item_from(deps, idep->valuestring);
                    // cJSON_DeleteItemFromObject(deps, idep->valuestring);
                    // printf("delete %s\n", idep->valuestring);
                }
            }
        }
    }
    // out = cJSON_Print(deps);
    // printf("deps %s\n", out);
    // free(out);
    return deps;
}

cJSON *update_deps(cJSON *state, cJSON *disables)
{
    cJSON *deps = get_depend();
    int ndeps = cJSON_GetArraySize(deps);
    int i;
    for(i = 0; i < ndeps; i++) {
        cJSON *dis = cJSON_GetArrayItem(deps, i);
        if(check_json_list(disables, dis->valuestring)) {
            cJSON_ReplaceItemInObject(state, dis->valuestring, cJSON_CreateString(DISABLE));
        } else {
            cJSON *st = cJSON_GetObjectItem(state, dis->valuestring);
            if(st->type == cJSON_String) {
                cJSON_ReplaceItemInObject(state, dis->valuestring, cJSON_CreateFalse());
            }
        }
    }
    cJSON_Delete(deps);
    return state;
}

cJSON *major_rule(cJSON *state, char *name, STATE action)
{
    set_state(state, name, action);
    // char *out = cJSON_Print(state);
    // printf("state is %s\n", out);
    // free(out);
    cJSON *major = get_major();
    cJSON *rela = cJSON_GetObjectItem(major, name);
    int size = cJSON_GetArraySize(rela);
    // printf("size of rela is %d\n", size);
    int i = 0;
    cJSON *deps = NULL;
    for(i; i < size; i++) {
        cJSON *item = cJSON_GetArrayItem(rela, i);
        // printf("%s -> %s\n", item->string, item->valuestring);
        if(item->type == cJSON_String && strcmp(item->valuestring, "exclusive") == 0) {
            cJSON_ReplaceItemInObject(state, item->string, cJSON_CreateFalse());
        }
    }
    cJSON *disables = get_disable_deps(state, major);
    update_deps(state, disables);
    cJSON_Delete(disables);
    cJSON_Delete(major);
    return state;
}

cJSON *Fun(cJSON *state, char *name, STATE action)
{
    if(check_depend(name)) {
        set_state(state, name, NIL);
    } else if(check_indep(name)) {
        set_state(state, name, action);
    } else if(check_major(name)) {
        major_rule(state, name, action);
    }
    return state;
}

cJSON *scene_check(cJSON *state)
{
    cJSON *sce = get_scene();
    int nsce = cJSON_GetArraySize(sce);
    int i;
    for(i = 0; i < nsce; i++) {
        cJSON *sitem = cJSON_GetArrayItem(sce, i);
        if(cJSON_GetObjectItem(state, sitem->string)->type == cJSON_True) {
            int nsitem = cJSON_GetArraySize(sitem);
            int j = 0;
            for(j = 0; j < nsitem; j++) {
                cJSON *action_item = cJSON_GetArrayItem(sitem, j);
                if(action_item->type == cJSON_True &
                cJSON_GetObjectItem(state, action_item->string)->type != cJSON_True) {
                    cJSON_ReplaceItemInObject(state, sitem->string, cJSON_CreateFalse());
                    break;
                }
            }
        }
    }
    return state;
}

cJSON *batch_fun(cJSON *state, char *sce_name, STATE action)
{
    set_state(state, sce_name, action);
    cJSON *sce = get_scene();
    cJSON *sce_item = cJSON_GetObjectItem(sce, sce_name);
    int nitem = cJSON_GetArraySize(sce_item);
    int i;
    for(i = 0; i < nitem; i++) {
        cJSON *st = cJSON_GetArrayItem(sce_item, i);
        if(st->type == cJSON_True) {
            Fun(state, st->string, action);
        }
    }
    cJSON_Delete(sce);
    return state;
}

int main(int argc, char const *argv[])
{
    /* code */
    cJSON *state = get_state();
    if (state == NULL) {
        perror("get state failed\n");
    }
    if(argc == 1) {

    } else {
        cJSON *item = cJSON_GetObjectItem(state, argv[1]);
        if(item->type == cJSON_String && (strcmp(item->valuestring, DISABLE) == 0)) {
            
        } else {
            if(check_scene(argv[1])) {
                //scene~
                cJSON *sce_state = cJSON_GetObjectItem(state, argv[1]);
                if(sce_state->type == cJSON_False) {
                    cJSON *sce = get_scene();
                    int nsce = cJSON_GetArraySize(sce);
                    int i = 0;
                    for(i = 0; i < nsce; i++) {
                        cJSON *s = cJSON_GetArrayItem(sce, i);
                        cJSON *st = cJSON_GetObjectItem(state, s->string);
                        if(st->type == cJSON_True) {
                            batch_fun(state, s->string, false);
                        }
                    }
                    batch_fun(state, argv[1], EN);
                } else {
                    batch_fun(state, argv[1], DIS);
                }
            } else {
                Fun(state, argv[1], NIL);
                scene_check(state);
                // not a scene
            }
        }
    }
    char *out = cJSON_PrintUnformatted(state);
    printf("%s\n", out);
    FILE *file = fopen(STATE_PATH, "w");
    fwrite(out, 1, strlen(out), file);
    fclose(file);

    free(out);
    cJSON_Delete(state);    
    return 0;
}
