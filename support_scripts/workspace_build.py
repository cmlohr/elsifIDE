import subprocess

# Directory where the main Cargo.toml (Workspace configuration) is located
workspace_dir = "path/to/workspace"

# Directory where the Svelte project is located
svelte_dir = f"{workspace_dir}/crates/ui/svelte"


# Build Rust workspace using Cargo
def build_rust_workspace():
    subprocess.run(["cargo", "build", "--release"], cwd=workspace_dir)
    print("Rust workspace built successfully!")


# Build Svelte project
def build_svelte():
    subprocess.run(["npm", "run", "build"], cwd=svelte_dir)
    print("Svelte project built successfully!")


def main():
    build_rust_workspace()
    build_svelte()
    print("Rust workspace and Svelte projects built successfully!")


if __name__ == "__main__":
    main()
