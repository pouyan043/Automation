## Features

- Clean old files based on age
- Download files from the internet (with streaming)
- Generate system reports
- YAML-based configuration
- Clean package structure with separated tasks

## Requirements

- Python 3.10+

## This is how to run

cd python-automation  
# venv\Scripts\activate     
 pip install -r requirements.txt  
 python main.py                    

## Configuration

Edit `config.yaml`:

```yaml
clean_dir: "./temp"
max_age_days: 7
download_url: "https://httpbin.org/robots.txt"
download_path: "./downloads/robots.txt"
```

## Usage

```bash
python main.py
# or with custom config
python main.py --config config.yaml
```

