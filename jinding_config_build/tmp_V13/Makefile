CONF_PATH:=../out/usr/share/
LUA_PATH:=../out/usr/bin
all:
	-mkdir -p $(CONF_PATH)
	-mkdir -p $(LUA_PATH)
	-cp -rf ./*.lua $(LUA_PATH)
	-cp -rf ./module $(CONF_PATH)
clean:
	rm -rf $(LUA_PATH)/*.lua
	rm -rf $(CONF_PATH)/module
.PHONY:  clean