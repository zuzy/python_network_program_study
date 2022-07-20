cmake_minimum_required(VERSION "3.14.4")

#############################
######### SOURCES ###########
#############################

set(DTU_CONF_PROTOC_EXECUTABLE "${CMAKE_BINARY_DIR}/bin/protoc")
#list(APPEND topspti_utils_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/utils/status.cc")
#list(APPEND topspti_utils_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/utils/utils.cc")
list(APPEND topspti_config_parser_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/config_parser.cc")
list(APPEND topspti_mq_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/mq.cc")
list(APPEND topspti_md5_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/md5.cc")
list(APPEND topspti_cpu_util_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/cpu/util.cc")
list(APPEND topspti_cpu_callstack_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/cpu/callstack.cc")
list(APPEND topspti_host_util_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/cpu/host_util.cc")
list(APPEND topspti_api_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/topspti_api.cc")
list(APPEND topspti_dpf_common_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/dpf_common.cc")
list(APPEND topspti_dpf_utils_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/dpf_utils.cc")
list(APPEND topspti_sip_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/sip_dpf.cc")
list(APPEND topspti_system_info_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/system_info.cc")
list(APPEND topspti_dma_dpf_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/dma_dpf.cc")
list(APPEND topspti_cqm_dpf_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/cqm_dpf.cc")
list(APPEND topspti_ts_dpf_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/ts_dpf.cc")
list(APPEND topspti_vdec_dpf_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/vdec_dpf.cc")
list(APPEND topspti_hcvg_dpf_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/hcvg_dpf.cc")
list(APPEND topspti_pcie_dpf_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/pcie_dpf.cc")
list(APPEND topspti_meta_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/meta.cc")
list(APPEND topspti_trace_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/trace.cc")
list(APPEND topspti_section_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/section.cc")
list(APPEND topspti_sw_ctrl_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/sw_ctrl.cc")
#list(APPEND topspti_reader_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/reader/data_reader.cc")
#list(APPEND topspti_reader_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/reader/profile_reader.cc")
#list(APPEND topspti_reader_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/reader/profile_adjuster.cc")
list(APPEND topspti_pavo_topspti_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/pavo/pavo_topspti.cc")
list(APPEND topspti_dorado_topspti_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/dorado/dorado_topspti.cc")
list(APPEND topspti_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/topspti.cc")
list(APPEND topspti_init_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/init.cc")
list(APPEND topspti_dtu20_sip_pmc_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/pmc/dtu20_sip_pmc.cc")
#list(APPEND topspti_pavo_dma_bpm_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/pavo/dtu20_dma_bpm.cc")
list(APPEND topspti_dtu20_pmc_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/dtu20_pmc.cc")
list(APPEND topspti_dtu20_pmc_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/dtu20_pmc_defs.cc")
list(APPEND topspti_sip_pmc_srcs "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/sip_pmc.cc")

list(APPEND topspti_common_dir "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/reader")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/reader")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/lib/profile/topspti")
list(APPEND topspti_common_dir "${CMAKE_SOURCE_DIR}/sdk/lib/dbgAPI/src")
list(APPEND topspti_common_dir "${CMAKE_SOURCE_DIR}/sdk/lib/dbgAPI/src/hwapi/mach")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/dbgAPI/src")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/lib/profile")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/lib")
list(APPEND topspti_common_dir "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/pavo")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/pavo")
list(APPEND topspti_common_dir "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/dorado")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/dorado")
list(APPEND topspti_common_dir "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/utils")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/utils")
list(APPEND topspti_common_dir "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/cpu")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/cpu")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/runtime/include") 
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/lib/profile/topspti/proto/database")
list(APPEND topspti_common_dir "${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/lib/profile/topspti/proto") 


###########################
######## TARGETS ##########
###########################

dtu_cc_library(
    NAME topspti_device
    LINK_DEPS topspti_global topspti_logging
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_pmc_device 
    LINK_DEPS topspti_device topspti_global
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_defs 
    LINK_DEPS topspti_logging topspti_dpf_defs topspti_pavo_dpf_id topspti_dorado_dpf_id topspti_obj topspti_sip_pmc_event
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_logging
    LINK_DEPS util
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_dpf_defs
    LINK_DEPS topspti_defs
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_pavo_dpf_id  
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_dorado_dpf_id 
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_global
    INCLUDES ${topspti_common_dir}
    LINK_DEPS topspti_defs topspti_logging topspti_dpf_defs topspti_pavo_dpf_id topspti_dorado_dpf_id topspti_obj topspti_sip_pmc_event
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_base 
    LINK_DEPS topspti_buf topspti_config_parser topspti_ctrl_cmd topspti_defs topspti_device topspti_dpf_common topspti_dpf_ctrl topspti_dpf_utils topspti_engine topspti_global topspti_header topspti_hw_ctrl_api topspti_impl topspti_irq topspti_logging topspti_md5 topspti_mq topspti_mutex topspti_obj topspti_reader topspti_sw_ctrl hwapi
    UTIL_DEPS topspti_topspti_proto topspti_database_proto
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_config_parser
    SRCS ${topspti_config_parser_srcs}
    LINK_DEPS topspti_logging topspti_utils
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_ctrl_cmd 
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_obj 
    LINK_DEPS topspti_defs
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_impl 
    LINK_DEPS topspti_device
    UTIL_DEPS topspti_database_proto
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_engine_impl 
    LINK_DEPS topspti_defs topspti_obj
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_engine 
    LINK_DEPS topspti_engine_impl topspti_obj topspti_utils
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_mutex 
    INCLUDES ${topspti_common_dir}
 
)
dtu_cc_library(
    NAME topspti_dpf_engine 
    LINK_DEPS topspti_dpf_common topspti_dpf_utils topspti_engine topspti_logging
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_pmc 
    LINK_DEPS topspti_dtu20_pmc topspti_engine
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_dma
    LINK_DEPS topspti_dpf_common topspti_dpf_engine topspti_dpf_utils topspti_global hwapi
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_cqm
    LINK_DEPS topspti_dpf_common topspti_dpf_engine topspti_dpf_utils hwapi
    INCLUDES ${topspti_common_dir}
)

dtu_cc_library(    
    NAME topspti_ts 
    LINK_DEPS topspti_dpf_common topspti_dpf_engine topspti_dpf_utils hwapi
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_sip
    LINK_DEPS topspti_dpf_common topspti_dpf_engine topspti_dpf_utils
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_hw_ctrl_api 
    LINK_DEPS topspti_logging hwapi
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_sip_pmc 
    SRCS ${topspti_sip_pmc_srcs}
    LINK_DEPS topspti_defs topspti_cqm topspti_base topspti_global topspti_logging topspti_dtu20_sip_pmc topspti_logging topspti_mutex topspti_pmc hwapi
    UTIL_DEPS topspti_topspti_proto 
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_sip_pmc_event
    INCLUDES ${topspti_common_dir}
    
)
dtu_cc_library(
    NAME topspti_pavo_dma
    LINK_DEPS topspti_defs topspti_dma topspti_obj
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_dorado_dma
    LINK_DEPS topspti_defs topspti_dma topspti_obj
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_hw_ctrl 
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_irq
    LINK_DEPS topspti_dpf_common topspti_dpf_utils topspti_logging
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_buf
    LINK_DEPS topspti_buf topspti_dpf_common topspti_dpf_defs topspti_hw_ctrl topspti_utils driver topspti_logging hwapi
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_dpf_ctrl
    LINK_DEPS topspti_api topspti_buf topspti_defs topspti_dpf_utils topspti_hw_ctrl topspti_hw_ctrl_api topspti_utils hwapi
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_header
    LINK_DEPS topspti_md5
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_dpf_handler
    LINK_DEPS topspti_logging topspti_dpf_defs topspti_sip_dpf topspti_dma_dpf topspti_cqm_dpf topspti_ts_dpf topspti_vdec_dpf topspti_hcvg_dpf topspti_pcie_dpf
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_utils
    SRCS_GLOB "utils/*.cc"
    INCLUDES ${topspti_common_dir}
   
)
dtu_cc_library(
    NAME topspti_mq
    SRCS ${topspti_mq_srcs}
    LINK_DEPS topspti_logging
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_md5
    SRCS ${topspti_md5_srcs}
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_cpu_util
    SRCS ${topspti_cpu_util_srcs}
    COPTS -fvisibility=default
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_cpu_callstack 
    SRCS ${topspti_cpu_callstack_srcs}
    LINK_DEPS topspti_api topspti_logging topspti_utils topspti_topspti_proto
    COPTS -fvisibility=default
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_host_util
    SRCS ${topspti_host_util_srcs}
    LINK_DEPS topspti_api topspti_defs topspti_global topspti_logging topspti_obj topspti_utils
    COPTS -fvisibility=default
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_api 
    SRCS ${topspti_api_srcs}
    LINK_DEPS topspti_defs topspti_global topspti_mutex topspti_md5 topspti_utils variant topspti_topspti_proto topspti_info_proto_cc
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
     NAME topspti_dpf_common 
     SRCS ${topspti_dpf_common_srcs}
     LINK_DEPS topspti_dpf_defs topspti_logging topspti_global
     INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_dpf_utils  
    SRCS ${topspti_dpf_utils_srcs}
    LINK_DEPS topspti_hw_ctrl_api topspti_defs topspti_global topspti_logging hwapi
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_sip_dpf
    SRCS ${topspti_sip_srcs}
    LINK_DEPS topspti_defs topspti_dpf_common topspti_logging topspti_global
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_system_info
    SRCS ${topspti_system_info_srcs}
    LINK_DEPS topspti_utils
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_dma_dpf 
    SRCS  ${topspti_dma_dpf_srcs}
    LINK_DEPS  topspti_defs topspti_dpf_common topspti_logging topspti_global
    INCLUDES ${topspti_common_dir}

)
dtu_cc_library(
    NAME topspti_cqm_dpf 
    SRCS ${topspti_cqm_dpf_srcs}
    LINK_DEPS topspti_defs topspti_dpf_common topspti_logging topspti_global
    INCLUDES ${topspti_common_dir}
    
)
dtu_cc_library(
    NAME topspti_ts_dpf 
    SRCS ${topspti_ts_dpf_srcs}
    LINK_DEPS topspti_defs topspti_dpf_common topspti_logging topspti_global
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_vdec_dpf
    SRCS ${topspti_vdec_dpf_srcs}
    LINK_DEPS topspti_defs topspti_dpf_common topspti_global topspti_logging
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_hcvg_dpf 
    SRCS ${topspti_hcvg_dpf_srcs}
    LINK_DEPS topspti_defs topspti_dpf_common topspti_global topspti_logging
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_pcie_dpf
    SRCS ${topspti_pcie_dpf_srcs}
    LINK_DEPS  topspti_dpf_common topspti_logging
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_meta
    SRCS ${topspti_meta_srcs}
    LINK_DEPS topspti_defs topspti_global topspti_mutex variant topspti_topspti_proto
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_trace
    SRCS ${topspti_trace_srcs}
    LINK_DEPS topspti_defs topspti_global topspti_mutex variant topspti_utils topspti_topspti_proto
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_section 
    SRCS ${topspti_section_srcs}
    LINK_DEPS topspti_defs topspti_global topspti_mutex topspti_api topspti_sw_ctrl topspti_topspti_proto
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_sw_ctrl
    SRCS ${topspti_sw_ctrl_srcs}
    LINK_DEPS  topspti_defs topspti_global topspti_mutex topspti_utils topspti_dpf_utils topspti_logging topspti_api topspti_system_info topspti_topspti_proto
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_reader
    SRCS_GLOB "reader/*.cc" 
    LINK_DEPS  topspti_utils topspti_dpf_handler topspti_api topspti_defs topspti_logging topspti_meta topspti_obj topspti_section topspti_header vdk_lib topspti_topspti_proto topspti_database_proto
    COPTS -lstdc++fs
    INCLUDES ${topspti_common_dir}

)
dtu_cc_library(
    NAME topspti_pavo_topspti
    SRCS ${topspti_pavo_topspti_srcs}
    LINK_DEPS topspti_base topspti_cqm topspti_defs topspti_device topspti_engine topspti_hw_ctrl_api topspti_logging topspti_pavo_dma topspti_pmc_device topspti_sip topspti_sip_pmc topspti_ts topspti_obj
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_dorado_topspti 
    SRCS ${topspti_dorado_topspti_srcs}
    LINK_DEPS topspti_base topspti_cqm topspti_defs topspti_device topspti_engine topspti_hw_ctrl_api topspti_logging topspti_dorado_dma topspti_pmc_device topspti_sip topspti_sip_pmc topspti_ts topspti_obj
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_
    SRCS ${topspti_srcs}
    LINK_DEPS topspti_base topspti_obj topspti_logging topspti_pavo_topspti topspti_dorado_topspti topspti_defs topspti_device driver topspti_database_proto
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_init 
    SRCS ${topspti_init_srcs}
    LINK_DEPS topspti_global topspti_ topspti_api
    UTIL_DEPS  topspti_database_proto
    INCLUDES ${topspti_common_dir}

)
dtu_cc_library(
    NAME topspti_pavo_dma_bpm
    SRCS "pavo/dtu20_dma_bpm.cc"
    LINK_DEPS  topspti_dtu20_pmc
    COPTS -D__PAVO__ -U__LEO__ -U__DORADO__
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library(
    NAME topspti_dtu20_sip_pmc
    SRCS ${topspti_dtu20_sip_pmc_srcs}
    LINK_DEPS topspti_dtu20_pmc
    COPTS -D__PAVO__ -U__LEO__ -D__DORADO__
    INCLUDES ${topspti_common_dir}
)
dtu_cc_library( 
    NAME topspti_dtu20_pmc 
    SRCS ${topspti_dtu20_pmc_srcs}
    LINK_DEPS  topspti_defs topspti_logging hwapi
    INCLUDES ${topspti_common_dir}
)
#CAI_E3:Function dtu_create_virtual_headers instead of dtu_file_gen
dtu_create_virtual_headers(
NAME proto_database_topspti
SRCS_GLOB "${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/proto/database/*"
DEST ${CMAKE_BINARY_DIR}/sdk/lib/profile/topspti/proto/database
) 


include(${CMAKE_SOURCE_DIR}/sdk/lib/profile/topspti/../proto.cmake)
define_proto(topspti2_proto_cc topspti2 lib/profile/topspti/proto)
define_proto(topspti_common_data_proto_cc topspti_common_data lib/profile/topspti/proto)
define_proto(topspti_info_proto_cc topspti_info lib/profile/topspti/proto)
define_proto(topspti_kernel_meta_proto_cc topspti_kernel_meta lib/profile/topspti/proto)
define_proto(topspti_memcpy_meta_proto_cc topspti_memcpy_meta lib/profile/topspti/proto)
define_proto(topspti_op_meta_proto_cc topspti_op_meta lib/profile/topspti/proto)
define_proto(topspti_packet_meta_proto_cc topspti_packet_meta lib/profile/topspti/proto)
define_proto(topspti_trace_event_proto_cc topspti_trace_event lib/profile/topspti/proto)
define_proto(DB_base_proto_cc base lib/profile/topspti/proto/database)
define_proto(DB_command_proto_cc command lib/profile/topspti/proto/database)
define_proto(DB_cpu_memory_utilization_proto_cc cpu_memory_utilization lib/profile/topspti/proto/database)
define_proto(DB_cpu_op_activity_proto_cc cpu_op_activity lib/profile/topspti/proto/database)
define_proto(DB_cpu_trace_activity_proto_cc cpu_trace_activity lib/profile/topspti/proto/database)
define_proto(DB_cpu_utilization_proto_cc cpu_utilization lib/profile/topspti/proto/database)
define_proto(DB_database_proto_cc database lib/profile/topspti/proto/database)
define_proto(DB_db_header_proto_cc db_header lib/profile/topspti/proto/database)
define_proto(DB_dtu_engine_activity_proto_cc dtu_engine_activity lib/profile/topspti/proto/database)
define_proto(DB_dtu_fw_activity_proto_cc dtu_fw_activity lib/profile/topspti/proto/database)
define_proto(DB_dtu_kernel_activity_proto_cc dtu_kernel_activity lib/profile/topspti/proto/database)
define_proto(DB_dtu_memcpy_activity_proto_cc dtu_memcpy_activity lib/profile/topspti/proto/database)
define_proto(DB_dtu_op_activity_proto_cc dtu_op_activity lib/profile/topspti/proto/database)
define_proto(DB_module_meta_proto_cc module_meta lib/profile/topspti/proto/database)
define_proto(DB_op_activity_proto_cc op_activity lib/profile/topspti/proto/database)
define_proto(DB_platform_proto_cc platform lib/profile/topspti/proto/database)
define_proto(DB_version_proto_cc version lib/profile/topspti/proto/database)


add_library(topspti STATIC
            $<TARGET_OBJECTS:topspti_config_parser>
            $<TARGET_OBJECTS:topspti_md5>
            $<TARGET_OBJECTS:topspti_dtu20_sip_pmc>
            $<TARGET_OBJECTS:topspti_dtu20_pmc>
            $<TARGET_OBJECTS:topspti_dpf_common>
            $<TARGET_OBJECTS:topspti_dpf_utils>
            $<TARGET_OBJECTS:topspti_sip_dpf>
            $<TARGET_OBJECTS:topspti_dma_dpf>
            $<TARGET_OBJECTS:topspti_cqm_dpf>
            $<TARGET_OBJECTS:topspti_ts_dpf>
            $<TARGET_OBJECTS:topspti_vdec_dpf>
            $<TARGET_OBJECTS:topspti_hcvg_dpf>
            $<TARGET_OBJECTS:topspti_pcie_dpf>
            $<TARGET_OBJECTS:topspti_reader>
            $<TARGET_OBJECTS:topspti_utils>
            $<TARGET_OBJECTS:topspti_mq>
            $<TARGET_OBJECTS:topspti_sw_ctrl>
            $<TARGET_OBJECTS:topspti_system_info>
            $<TARGET_OBJECTS:topspti_cpu_util>
            $<TARGET_OBJECTS:topspti_cpu_callstack>
            $<TARGET_OBJECTS:topspti_host_util>
            $<TARGET_OBJECTS:topspti_api>
            $<TARGET_OBJECTS:topspti_section>
            $<TARGET_OBJECTS:topspti_meta>
            $<TARGET_OBJECTS:topspti_pavo_topspti>
            $<TARGET_OBJECTS:topspti_dorado_topspti>
            $<TARGET_OBJECTS:topspti_trace>
            $<TARGET_OBJECTS:topspti_>
            $<TARGET_OBJECTS:topspti_sip_pmc>
)

add_library(topspti_topspti_proto STATIC
            $<TARGET_OBJECTS:topspti2_proto_cc>
            $<TARGET_OBJECTS:topspti_common_data_proto_cc>
            $<TARGET_OBJECTS:topspti_info_proto_cc>
            $<TARGET_OBJECTS:topspti_kernel_meta_proto_cc>
            $<TARGET_OBJECTS:topspti_memcpy_meta_proto_cc>
            $<TARGET_OBJECTS:topspti_packet_meta_proto_cc>
            $<TARGET_OBJECTS:topspti_op_meta_proto_cc>
            $<TARGET_OBJECTS:topspti_trace_event_proto_cc>
)
add_library(topspti_database_proto STATIC
            $<TARGET_OBJECTS:DB_base_proto_cc>
            $<TARGET_OBJECTS:DB_command_proto_cc>
            $<TARGET_OBJECTS:DB_cpu_memory_utilization_proto_cc>
            $<TARGET_OBJECTS:DB_cpu_op_activity_proto_cc>
            $<TARGET_OBJECTS:DB_cpu_trace_activity_proto_cc>
            $<TARGET_OBJECTS:DB_cpu_utilization_proto_cc>
            $<TARGET_OBJECTS:DB_database_proto_cc>
            $<TARGET_OBJECTS:DB_db_header_proto_cc>
            $<TARGET_OBJECTS:DB_dtu_engine_activity_proto_cc>
            $<TARGET_OBJECTS:DB_dtu_fw_activity_proto_cc>
            $<TARGET_OBJECTS:DB_dtu_kernel_activity_proto_cc>
            $<TARGET_OBJECTS:DB_dtu_memcpy_activity_proto_cc>
            $<TARGET_OBJECTS:DB_dtu_op_activity_proto_cc>
            $<TARGET_OBJECTS:DB_module_meta_proto_cc>
            $<TARGET_OBJECTS:DB_op_activity_proto_cc>
            $<TARGET_OBJECTS:DB_platform_proto_cc>
            $<TARGET_OBJECTS:DB_version_proto_cc>
)

add_dependencies(topspti2_proto_cc topspti_common_data_proto_cc)
add_dependencies(topspti2_proto_cc topspti_info_proto_cc)
add_dependencies(topspti2_proto_cc topspti_op_meta_proto_cc)
add_dependencies(topspti2_proto_cc topspti_kernel_meta_proto_cc)
add_dependencies(topspti2_proto_cc topspti_memcpy_meta_proto_cc)
add_dependencies(topspti2_proto_cc topspti_packet_meta_proto_cc)
add_dependencies(topspti2_proto_cc topspti_trace_event_proto_cc)
add_dependencies(topspti_info_proto_cc topspti_common_data_proto_cc)
add_dependencies(topspti_kernel_meta_proto_cc topspti_common_data_proto_cc)
add_dependencies(topspti_kernel_meta_proto_cc topspti_packet_meta_proto_cc)
add_dependencies(topspti_memcpy_meta_proto_cc topspti_common_data_proto_cc)
add_dependencies(topspti_memcpy_meta_proto_cc topspti_packet_meta_proto_cc)
add_dependencies(topspti_op_meta_proto_cc topspti_common_data_proto_cc)
add_dependencies(topspti_trace_event_proto_cc topspti_common_data_proto_cc)
add_dependencies(DB_cpu_memory_utilization_proto_cc DB_base_proto_cc)
add_dependencies(DB_cpu_op_activity_proto_cc DB_op_activity_proto_cc)
add_dependencies(DB_cpu_trace_activity_proto_cc DB_base_proto_cc)
add_dependencies(DB_cpu_utilization_proto_cc DB_base_proto_cc)
add_dependencies(DB_database_proto_cc DB_base_proto_cc)
add_dependencies(DB_database_proto_cc DB_command_proto_cc)
add_dependencies(DB_database_proto_cc DB_cpu_memory_utilization_proto_cc)
add_dependencies(DB_database_proto_cc DB_cpu_op_activity_proto_cc)
add_dependencies(DB_database_proto_cc DB_cpu_trace_activity_proto_cc)
add_dependencies(DB_database_proto_cc DB_cpu_utilization_proto_cc)
add_dependencies(DB_database_proto_cc DB_db_header_proto_cc)
add_dependencies(DB_database_proto_cc DB_dtu_fw_activity_proto_cc)
add_dependencies(DB_database_proto_cc DB_dtu_kernel_activity_proto_cc)
add_dependencies(DB_database_proto_cc DB_dtu_memcpy_activity_proto_cc)
add_dependencies(DB_database_proto_cc DB_dtu_op_activity_proto_cc)
add_dependencies(DB_database_proto_cc DB_module_meta_proto_cc)
add_dependencies(DB_database_proto_cc DB_platform_proto_cc)
add_dependencies(DB_database_proto_cc DB_version_proto_cc)
add_dependencies(DB_dtu_engine_activity_proto_cc DB_base_proto_cc)
add_dependencies(DB_dtu_fw_activity_proto_cc DB_dtu_engine_activity_proto_cc)
add_dependencies(DB_dtu_kernel_activity_proto_cc DB_dtu_engine_activity_proto_cc)
add_dependencies(DB_dtu_memcpy_activity_proto_cc DB_dtu_engine_activity_proto_cc)
add_dependencies(DB_dtu_op_activity_proto_cc DB_base_proto_cc)
add_dependencies(DB_dtu_op_activity_proto_cc DB_op_activity_proto_cc)
add_dependencies(DB_op_activity_proto_cc DB_base_proto_cc)

