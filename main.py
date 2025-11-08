import tomli
import sys

CONFIG_FILE = "config.toml"

def load_config():
    required_keys = [
        "package_name",
        "repo_url",
        "repo_mode",
        "ascii_mode",
        "filter_substring"
    ]

    try:
        with open(CONFIG_FILE, "rb") as f:
            cfg = tomli.load(f)
    except FileNotFoundError:
        sys.exit(f"Error: configuration file '{CONFIG_FILE}' not found.")
    except tomli.TOMLDecodeError as e:
        sys.exit(f"Error: invalid TOML format — {e}")
    except Exception as e:
        sys.exit(f"Error while loading configuration: {e}")

    for key in required_keys:
        if key not in cfg:
            sys.exit(f"Error: missing required parameter '{key}' in configuration.")

    return cfg


def main():
    cfg = load_config()

    print("=== Application Configuration ===")
    for key, value in cfg.items():
        print(f"{key} = {value}")
    print("=================================")

    print("\nConfiguration successfully loaded and validated.")


if __name__ == "__main__":
    main()
