proto_library(
    name = "topspti_proto",
    srcs = glob(["proto/*.proto"])
)

cc_proto_library(
  name = "topspti_cc_proto",
  deps = [":topspti_proto"],
)

proto_library(
    name = "database_proto",
    srcs = glob(["proto/database/*.proto"])
)

cc_proto_library(
    name = "database_cc_proto",
    deps = [":database_proto"],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "device",
    hdrs = [
        "device.h",
    ],
    deps = [
        ":global",
        ":logging",
    ],
)

cc_library(
    name = "pmc_device",
    hdrs = [
        "pmc_device.h",
    ],
    deps = [
        ":device",
        ":global",
    ],
)

cc_library(
    name = "md5",
    srcs = [
        "md5.cc",
    ],
    hdrs = [
        "md5.h",
    ],
)

cc_library(
    name = "header",
    hdrs = [
        "header.h",
    ],
    deps = [
        "md5",
    ],
)

cc_library(
    name = "mutex",
    hdrs = [
        "mutex.h",
    ],
)

cc_library(
    name = "logging",
    hdrs = ["logging.h"],
    deps = [
        "//lib:util",
    ],
)

cc_library(
    name = "irq",
    hdrs = [
        "irq.h",
    ],
    deps = [
        ":dpf_common",
        ":dpf_utils",
        ":logging",
        "//lib/umd/include",
    ],
)

cc_library(
    name = "buf",
    hdrs = [
        "buf.h",
    ],
    deps = [
        ":dpf_common",
        ":dpf_defs",
        ":hw_ctrl",
        ":utils",
        ":logging",
        "//lib/dbgAPI/src:hwapi",
    ],
)

cc_library(
    name = "config_parser",
    srcs = [
        "config_parser.cc",
    ],
    hdrs = [
        "config_parser.h",
    ],
    deps = [
        ":logging",
        ":utils",
    ],
)

cc_library(
    name = "defs",
    hdrs = ["defs.h"],
    deps = [
    ],
)

cc_library(
    name = "global",
    hdrs = ["global.h"],
    deps = [
        ":defs",
        ":logging",
        ":dpf_defs",
        ":pavo_dpf_id",
        ":dorado_dpf_id",
        ":obj",
        ":sip_pmc_event",
    ],
)

cc_library(
    name = "base",
    hdrs = [
        "base.h",
    ],
    deps = [
        ":buf",
        ":config_parser",
        ":cpu",
        ":ctrl_cmd",
        ":database_cc_proto",
        ":defs",
        ":device",
        ":dpf_common",
        ":dpf_ctrl",
        ":dpf_utils",
        ":engine",
        ":global",
        ":header",
        ":hw_ctrl_api",
        ":impl",
        ":irq",
        ":logging",
        ":md5",
        ":mq",
        ":mutex",
        ":obj",
        ":reader",
        ":sw_ctrl",
        ":topspti_cc_proto",
        "//lib/dbgAPI/src:hwapi",
    ],
)

cc_library(
    name = "pavo_dpf_id",
    srcs = [
        "pavo/dpf_id.inc",
    ],
)

cc_library(
    name = "dorado_dpf_id",
    srcs = [
        "dorado/dpf_id.inc",
    ],
)

cc_library(
    name = "init",
    srcs = [
        "init.cc",
    ],
    deps = [
        ":global",
        ":topspti",
        ":api",
    ],
    alwayslink = True,
    visibility = ["//visibility:public"],
)

cc_library(
    name = "hw_ctrl",
    hdrs = [
        "hw_ctrl.h",
    ],
    deps = [
    ],
)

cc_library(
    name = "hw_ctrl_api",
    hdrs = [
        "hw_ctrl_api.h",
    ],
    deps = [
        "//lib/dbgAPI/src:hwapi",
        ":logging",
    ],
)

cc_library(
    name = "dpf_defs",
    hdrs = [
        "dpf_defs.h",
    ],
    deps = [
        ":defs",
    ],
)

cc_library(
    name = "dpf_common",
    srcs = [
        "dpf_common.cc",
    ],
    hdrs = [
        "dpf_common.h",
    ],
    deps = [
        ":dpf_defs",
        ":logging",
        ":global",
    ],
)

cc_library(
    name = "dtu20_pmc",
    srcs = [
        "dtu20_pmc.cc",
        "dtu20_pmc_defs.cc"
    ],
    hdrs = [
        "dtu20_pmc.h",
        "dtu20_pmc_defs.h"
    ],
    deps = [
        ":defs",
        ":logging",
        "//lib/dbgAPI/src:hwapi",
    ],
)

cc_library(
    name = "dpf_utils",
    hdrs = [
        "dpf_utils.h",
    ],
    srcs = [
        "dpf_utils.cc",
    ],
    deps = [
        ":hw_ctrl_api",
        ":defs",
        ":global",
        ":logging",
        "//lib/dbgAPI/src:hwapi",
    ],
)

cc_library(
    name = "system_info",
    hdrs = [
        "system_info.h",
    ],
    srcs = [
        "system_info.cc",
    ],
    deps = [
        ":utils",
    ],
)

cc_library(
    name = "sip_dpf",
    srcs = [
        "sip_dpf.cc",
    ],
    hdrs = [
        "sip_dpf.h",
    ],
    deps = [
        ":defs",
        ":dpf_common",
        ":logging",
        ":global",
    ],
)

cc_library(
    name = "dma_dpf",
    srcs = [
        "dma_dpf.cc",
    ],
    hdrs = [
        "dma_dpf.h",
    ],
    deps = [
        ":defs",
        ":dpf_common",
        ":logging",
        ":global",
    ],
)

cc_library(
    name = "cqm_dpf",
    srcs = [
        "cqm_dpf.cc",
    ],
    hdrs = [
        "cqm_dpf.h",
    ],
    deps = [
        ":defs",
        ":dpf_common",
        ":logging",
        ":global",
    ],
)

cc_library(
    name = "ts_dpf",
    srcs = [
        "ts_dpf.cc",
    ],
    hdrs = [
        "ts_dpf.h",
    ],
    deps = [
        ":defs",
        ":dpf_common",
        ":global",
        ":logging",
    ],
)

cc_library(
    name = "vdec_dpf",
    srcs = [
        "vdec_dpf.cc",
    ],
    hdrs = [
        "vdec_dpf.h",
    ],
    deps = [
        ":defs",
        ":dpf_common",
        ":global",
        ":logging",
    ],
)

cc_library(
    name = "hcvg_dpf",
    srcs = [
        "hcvg_dpf.cc",
    ],
    hdrs = [
        "hcvg_dpf.h",
    ],
    deps = [
        ":defs",
        ":dpf_common",
        ":global",
        ":logging",
    ],
)

cc_library(
    name = "pcie_dpf",
    srcs = [
        "pcie_dpf.cc",
    ],
    hdrs = [
        "pcie_dpf.h",
    ],
    deps = [
        ":dpf_common",
        ":logging",
    ],
)

cc_library(
    name = "trace",
    hdrs = [
        "trace.h",
    ],
    srcs = [
        "trace.cc",
    ],
    deps = [
        ":defs",
        ":global",
        ":mutex",
        ":utils",
        ":topspti_cc_proto",
        "//lib/profile:variant",
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "dpf_handler",
    hdrs = [
        "dpf_handler.h",
    ],
    deps = [
        ":logging",
        ":dpf_defs",
        ":sip_dpf",
        ":dma_dpf",
        ":cqm_dpf",
        ":ts_dpf",
        ":vdec_dpf",
        ":hcvg_dpf",
        ":pcie_dpf",
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "reader",
    hdrs = glob([
        "reader/*.h",
    ]),
    srcs = glob([
        "reader/*.cc",
    ]),
    deps = [
        ":database_cc_proto",
        ":utils",
        ":dpf_handler",
        ":topspti_cc_proto",
        ":api",
        ":defs",
        ":global",
        ":logging",
        ":meta",
        ":obj",
        ":section",
        ":header",
        "//lib:dtu_umd"
    ],
    linkopts = ["-lstdc++fs"],
    includes = ["."],
)

cc_library(
    name = "utils",
    hdrs = glob([
        "utils/*.h",
    ]),
    srcs = glob([
        "utils/*.cc",
    ]),
)

cc_library(
    name = "mq",
    hdrs = [
        "mq.h",
    ],
    srcs = [
        "mq.cc",
    ],
    deps = [
        ":logging",
    ],
)

cc_library(
    name = "ctrl_cmd",
    hdrs = [
        "ctrl_cmd.h",
    ],
    deps = [
    ],
)

cc_library(
    name = "obj",
    hdrs = [
        "obj.h",
    ],
    deps = [
        ":defs",
    ],
)

cc_library(
    name = "impl",
    hdrs = [
        "impl.h",
    ],
    deps = [
        ":device",
        ":database_cc_proto",
    ],
)

cc_library(
    name = "engine_impl",
    hdrs = [
        "engine_impl.h",
    ],
    deps = [
        ":defs",
        ":obj",
    ],
)

cc_library(
    name = "engine",
    hdrs = [
        "engine.h",
    ],
    deps = [
        ":engine_impl",
        ":obj",
        ":utils",
    ],
)

cc_library(
    name = "dpf_engine",
    hdrs = [
        "dpf_engine.h",
    ],
    deps = [
        ":dpf_common",
        ":dpf_utils",
        ":engine",
        ":logging",
    ],
)

cc_library(
    name = "pmc",
    hdrs = [
        "pmc.h",
    ],
    deps = [
        ":dtu20_pmc",
        ":engine",
    ],
)

cc_library(
    name = "dma",
    hdrs = [
        "dma.h",
    ],
    deps = [
        ":dpf_common",
        ":dpf_engine",
        ":dpf_utils",
        ":global",
        "//lib/dbgAPI/src:hwapi",
    ],
)

cc_library(
    name = "cqm",
    hdrs = [
        "cqm.h",
    ],
    deps = [
        ":dpf_common",
        ":dpf_engine",
        ":dpf_utils",
        "//lib/dbgAPI/src:hwapi",
    ],
)

cc_library(
    name = "pavo_dma_bpm",
    hdrs = [
        "pavo/dtu20_dma_bpm.h",
    ],
    srcs = glob([
        "pavo/dtu20_dma_bpm.cc",
    ]),
    copts = ["-U__LEO__ -U__DORAOD__"],
    deps = [
        ":dtu20_pmc",
    ],
    # TODO (cuibixiong) temporary for testing.
    visibility = ["//visibility:public"],
)

cc_library(
    name = "ts",
    hdrs = [
        "ts.h",
    ],
    deps = [
        ":dpf_common",
        ":dpf_engine",
        ":dpf_utils",
        "//lib/dbgAPI/src:hwapi",
    ],
)

cc_library(
    name = "sip",
    hdrs = [
        "sip.h",
    ],
    deps = [
        ":dpf_common",
        ":dpf_engine",
        ":dpf_utils",
    ],
)

cc_library(
    name = "dtu20_sip_pmc",
    hdrs = [
        "pmc/dtu20_sip_pmc.h",
    ],
    srcs = glob([
        "pmc/dtu20_sip_pmc.cc",
    ]),
    copts = ["-U__LEO__"],
    deps = [
        ":dtu20_pmc",
    ],
    # TODO (cuibixiong) temporary for testing.
    visibility = ["//visibility:public"],
)

cc_library(
    name = "pavo_dma_pmc",
    hdrs = [
        "pavo/dtu20_dma_pmc.h",
    ],
    srcs = glob([
        "pavo/dtu20_dma_pmc.cc",
    ]),
    copts = ["-U__LEO__ -U__DORAOD__"],
    deps = [
        ":dtu20_sip_pmc",
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "dorado_dma_pmc",
    hdrs = [
        "dorado/dorado_dma_pmc.h",
        "dorado/dorado_pmc_defs.h"
    ],
    srcs = glob([
        "dorado/dorado_dma_pmc.cc",
        "dorado/dorado_pmc_defs.cc"
    ]),
    copts = ["-U__LEO__ -U__DORAOD__"],
    deps = [
        ":pavo_dma_pmc",
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "sip_pmc",
    srcs = [
        "sip_pmc.cc",
    ],
    hdrs = [
        "sip_pmc.h",
    ],
    deps = [
        ":defs",
        ":cqm",
        ":base",
        ":global",
        ":dtu20_sip_pmc",
        ":logging",
        ":mutex",
        ":pmc",
        ":topspti_cc_proto",
        "//lib/dbgAPI/src:hwapi",
    ],
)

cc_library(
    name = "sip_pmc_event",
    srcs = [
        "sip_pmc_event.inc",
    ],
)

cc_library(
    name = "dma_pmc",
    hdrs = [
        "sip_pmc.h",
    ],
    deps = [
        ":defs",
        ":global",
        ":dtu20_sip_pmc",
        ":logging",
        ":mutex",
        ":pmc",
        ":topspti_cc_proto",
        "//lib/dbgAPI/src:hwapi",
    ],
)


cc_library(
    name = "pavo_dma",
    hdrs = [
        "pavo/dma.h",
    ],
    deps = [
        ":defs",
        ":dma",
        ":obj",
    ],
)

cc_library(
    name = "dorado_dma",
    hdrs = [
        "dorado/dma.h",
    ],
    deps = [
        ":defs",
        ":dma",
        ":obj",
    ],
)

cc_library(
    name = "dpf_ctrl",
    hdrs = [
        "dpf_ctrl.h",
    ],
    deps = [
        ":api",
        ":buf",
        ":defs",
        ":dpf_utils",
        ":hw_ctrl",
        ":hw_ctrl_api",
        ":utils",
        "//lib/dbgAPI/src:hwapi",
    ],
)

cc_library(
    name = "sw_ctrl",
    hdrs = [
        "sw_ctrl.h",
    ],
    srcs = [
        "sw_ctrl.cc",
    ],
    deps = [
        ":defs",
        ":global",
        ":mutex",
        ":utils",
        ":dpf_utils",
        ":logging",
        ":api",
        ":system_info",
        ":topspti_cc_proto",
    ],
)

cc_library(
    name = "cpu_util",
    hdrs = [
        "cpu/util.h",
    ],
    srcs = [
        "cpu/util.cc",
    ],
    deps = [
        ":api",
        ":defs",
        ":logging",
        ":utils",
    ],
)

cc_library(
    name = "cpu_callstack",
    hdrs = [
        "cpu/callstack.h",
    ],
    srcs = [
        "cpu/callstack.cc",
    ],
    deps = [
        ":api",
        ":logging",
        ":topspti_cc_proto",
        ":utils",
    ],
)

cc_library(
    name = "host_util",
    hdrs = [
        "cpu/host_util.h",
    ],
    srcs = [
        "cpu/host_util.cc",
    ],
    deps = [
        ":api",
        ":defs",
        ":global",
        ":logging",
        ":obj",
        ":utils",
    ],
)

cc_library(
    name = "cpu",
    hdrs = [
        "cpu/cpu.h",
    ],
    deps = [
        ":defs",
        ":engine",
        ":obj",
        ":cpu_util",
        ":cpu_callstack",
        ":dpf_utils",
        ":host_util",
        ":system_info",
        ":utils",
    ],
)

cc_library(
    name = "api",
    hdrs = [
        "topspti_api.h",
    ],
    srcs = [
        "topspti_api.cc",
    ],
    deps = [
        ":defs",
        ":global",
        ":mutex",
        ":md5",
        ":utils",
        ":topspti_cc_proto",
        "//lib/profile:variant",
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "section",
    hdrs = [
        "section.h",
    ],
    srcs = [
        "section.cc",
    ],
    deps = [
        "//lib/umd/include",
        ":defs",
        ":global",
        ":mutex",
        ":topspti_cc_proto",
        ":sw_ctrl",
        ":api",
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "meta",
    hdrs = [
        "meta.h",
    ],
    srcs = [
        "meta.cc",
    ],
    deps = [
        ":defs",
        ":global",
        ":mutex",
        ":topspti_cc_proto",
        "//lib/profile:variant",
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "pavo_topspti",
    hdrs = [
        "pavo/pavo_topspti.h",
    ],
    srcs = [
        "pavo/pavo_topspti.cc",
    ],
    deps = [
        ":base",
        ":cqm",
        ":defs",
        ":device",
        ":engine",
        ":hw_ctrl_api",
        ":logging",
        ":pavo_dma",
        ":pmc_device",
        ":sip",
        ":sip_pmc",
        ":ts",
        ":obj",
    ],
)

cc_library(
    name = "dorado_topspti",
    hdrs = [
        "dorado/dorado_topspti.h",
    ],
    srcs = [
        "dorado/dorado_topspti.cc",
    ],
    deps = [
        ":base",
        ":cqm",
        ":defs",
        ":device",
        ":engine",
        ":hw_ctrl_api",
        ":logging",
        ":dorado_dma",
        ":pmc_device",
        ":sip",
        ":sip_pmc",
        ":ts",
        ":obj",
    ],
)

cc_library(
    name = "topspti",
    hdrs = [
        "topspti.h",
    ],
    srcs = ["topspti.cc"],
    deps = [
        ":base",
        ":obj",
        ":logging",
        ":dorado_topspti",
        ":pavo_topspti",
        ":defs",
        ":device",
        ":trace",
        ":database_cc_proto",
    ],
    visibility = ["//visibility:public"],
)

cc_binary(
    name = "topspti_demo",
    srcs = ["topspti_demo.cc"],
    deps = [
        ":topspti",
    ],
)

