use askama::Template;


#[derive(Template)]
#[template(path = "Rte.h", escape = "none")]
struct HeaderTemplate<'a> {
    functions: &'a [FunctionSpec],
    variables: &'a [VariableSpec],
}

struct FunctionSpec {
    name: String,
    args: String,
}

struct VariableSpec {
    ctype: String,
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

    let header = HeaderTemplate {
        functions: &funcs,
        variables: &vars,
    };

    let rendered = header.render().unwrap();
    std::fs::write("Rte.h", rendered).unwrap();
}
