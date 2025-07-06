use askama::Template;

#[derive(Template)]
#[template(path = "Rte.h", escape = "none")]
struct HeaderTemplate<'a> {
    functions: &'a [FunctionSpec],
    variables: &'a [VariableSpec],
    ports: &'a [PortSpec],
    pims: &'a [PimSpec],
    irvs: &'a [IrvSpec],
    modes: &'a [ModeSpec],
    triggers: &'a [TriggerSpec],
}

struct FunctionSpec {
    name: String,
    args: String,
}

struct VariableSpec {
    ctype: String,
    name: String,
}

#[derive(Debug, PartialEq)]
pub enum PortType {
    ClientServer,
    SenderReceiver,
}

impl PortType {
    pub fn as_str(&self) -> &str {
        match self {
            PortType::ClientServer => "ClientServer",
            PortType::SenderReceiver => "SenderReceiver",
        }
    }
}

struct PortSpec {
    name: String,
    signal: String,
    port_type: PortType,
}

impl PortSpec {
    pub fn kind(&self) -> &str {
        self.port_type.as_str()
    }
}

struct PimSpec {
    name: String,
    ctype: String,
}

struct IrvSpec {
    runnable: String,
    name: String,
    ctype: String,
}

struct ModeSpec {
    name: String,
    mode_values: Vec<String>,
}

struct TriggerSpec {
    name: String,
}

fn main() {
    let funcs = vec![
        FunctionSpec {
            name: "InitSystem".to_string(),
            args: "void".to_string(),
        },
        FunctionSpec {
            name: "ProcessData".to_string(),
            args: "int data".to_string(),
        },
    ];

    let vars = vec![
        VariableSpec {
            ctype: "int".to_string(),
            name: "system_ready".to_string(),
        },
        VariableSpec {
            ctype: "char".to_string(),
            name: "buffer[256]".to_string(),
        },
    ];

    let ports = vec![
        PortSpec {
            name: "first_port".to_string(),
            signal: "data_out".to_string(),
            port_type: PortType::SenderReceiver,
        },
        PortSpec {
            name: "second_port".to_string(),
            signal: "command".to_string(),
            port_type: PortType::ClientServer,
        },
    ];

    let pims = vec![
        PimSpec {
            name: "internal_state".to_string(),
            ctype: "uint8".to_string(),
        },
    ];

    let irvs = vec![
        IrvSpec {
            runnable: "ProcessData".to_string(),
            name: "temp_buffer".to_string(),
            ctype: "uint16".to_string(),
        },
    ];

    let modes = vec![
        ModeSpec {
            name: "SystemMode".to_string(),
            mode_values: vec!["INIT".to_string(), "RUN".to_string(), "SLEEP".to_string()],
        },
    ];

    let triggers = vec![
        TriggerSpec {
            name: "WatchdogKick".to_string(),
        },
    ];

    let header = HeaderTemplate {
        functions: &funcs,
        variables: &vars,
        ports: &ports,
        pims: &pims,
        irvs: &irvs,
        modes: &modes,
        triggers: &triggers,
    };

    let rendered = header.render().unwrap();
    std::fs::create_dir_all("rtegen").unwrap();
    std::fs::write("rtegen/Rte.h", rendered).unwrap();
    std::fs::copy("templates/Rte_Type.h", "rtegen/Rte_Type.h").unwrap();
    std::fs::copy("templates/Std_Types.h", "rtegen/Std_Types.h").unwrap();
    std::fs::copy("templates/Platform_Types.h", "rtegen/Platform_Types.h").unwrap();
    std::fs::copy("templates/Compiler.h", "rtegen/Compiler.h").unwrap();
}
