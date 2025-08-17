from cli.cpi_commands.auth import get_oauth_token, get_csrf_token, get_cpi_credentials
import requests
import json
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os
import zipfile
import base64

console = Console()

def list_artifacts():
    """Lists all integration runtime artifacts from SAP CPI."""
    credentials = get_cpi_credentials()
    if not credentials:
        return

    access_token = get_oauth_token()
    if not access_token:
        return

    csrf_token = get_csrf_token(access_token)
    if not csrf_token:
        return

    base_url = credentials['url']
    url = f"{base_url}/api/v1/IntegrationRuntimeArtifacts"

    headers = {
        'X-CSRF-Token': csrf_token,
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    try:
        with console.status("[bold green]Fetching integration runtime artifacts...[/bold green]"):
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

        artifacts = data.get("d", {}).get("results", [])

        if not artifacts:
            console.print(Panel("[bold yellow]No integration runtime artifacts found.[/bold yellow]", title="[bold cyan]CPI Integration Artifacts[/bold cyan]", border_style="cyan"))
            return

        table = Table(show_header=True, header_style="bold green")
        table.add_column("Artifact Name", style="bold magenta")
        table.add_column("Artifact ID", style="bold blue")


        for artifact in artifacts:
            artifact_name = artifact.get("Name", "N/A")
            artifact_id = artifact.get("Id", "N/A")
            table.add_row(artifact_name, artifact_id)

        console.print(Panel(table, title="[bold cyan]CPI Integration Artifacts[/bold cyan]", border_style="cyan"))

    except requests.exceptions.RequestException as e:
        console.print(Panel(f"[bold red]Error listing artifacts: {e}[/bold red]", title="[bold red]Error[/bold red]", border_style="red"))
    except Exception as e:
        console.print(Panel(f"[bold red]An unexpected error occurred: {e}[/bold red]", title="[bold red]Error[/bold red]", border_style="red"))

def download_artifact(artifact_id: str, version: str = 'active'):
    """Downloads a specific integration artifact by its ID."""
    credentials = get_cpi_credentials()
    if not credentials:
        return

    access_token = get_oauth_token()
    if not access_token:
        return

    csrf_token = get_csrf_token(access_token)
    if not csrf_token:
        return

    base_url = credentials['url']
    url = f"{base_url}/api/v1/IntegrationDesigntimeArtifacts(Id='{artifact_id}',Version='{version}')/$value"

    headers = {
        'X-CSRF-Token': csrf_token,
        'Accept': 'application/zip',
        'Authorization': f'Bearer {access_token}'
    }

    try:
        with console.status(f"[bold green]Downloading artifact {artifact_id}...[/bold green]"):
            response = requests.get(url, headers=headers)
            response.raise_for_status()

        # Save the zip file
        save_dir = "cpi_downloads"
        os.makedirs(save_dir, exist_ok=True)
        zip_path = os.path.join(save_dir, f"{artifact_id}.zip")
        with open(zip_path, 'wb') as f:
            f.write(response.content)
        console.print(Panel(f"[bold green]Artifact '{artifact_id}' downloaded successfully to {zip_path}[/bold green]", title="[bold cyan]Download Complete[/bold cyan]", border_style="cyan"))

        # Extract the zip file
        extract_dir = os.path.join(save_dir, artifact_id)
        os.makedirs(extract_dir, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        console.print(Panel(f"[bold green]Artifact extracted to {extract_dir}[/bold green]", title="[bold cyan]Extraction Complete[/bold cyan]", border_style="cyan"))


    except requests.exceptions.RequestException as e:
        console.print(Panel(f"[bold red]Error downloading artifact: {e}[/bold red]", title="[bold red]Error[/bold red]", border_style="red"))
    except Exception as e:
        console.print(Panel(f"[bold red]An unexpected error occurred: {e}[/bold red]", title="[bold red]Error[/bold red]", border_style="red"))


def deploy_artifact(file_path: str, artifact_id: str, artifact_name: str, package_id: str):
    """Deploys an integration artifact (iFlow) to SAP CPI."""
    credentials = get_cpi_credentials()
    if not credentials:
        return

    access_token = get_oauth_token()
    if not access_token:
        return

    csrf_token = get_csrf_token(access_token)
    if not csrf_token:
        return

    try:
        with open(file_path, 'rb') as f:
            content = f.read()
    except FileNotFoundError:
        console.print(Panel(f"[bold red]Error: File not found at {file_path}[/bold red]", title="[bold red]Error[/bold red]", border_style="red"))
        return

    base_url = credentials['url']
    url = f"{base_url}/api/v1/IntegrationDesigntimeArtifacts"

    headers = {
        'X-CSRF-Token': csrf_token,
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    metadata = {
        "Id": artifact_id,
        "Name": artifact_name or artifact_id,
        "PackageId": package_id
    }

    payload = {
        **metadata,
        "ArtifactContent": base64.b64encode(content).decode('utf-8')
    }

    try:
        with console.status(f"[bold green]Deploying artifact {artifact_id}...[/bold green]"):
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
        console.print(Panel(f"[bold green]Artifact '{artifact_id}' deployed successfully![/bold green]", title="[bold cyan]Deployment Complete[/bold cyan]", border_style="cyan"))

    except requests.exceptions.RequestException as e:
        console.print(Panel(f"[bold red]Error deploying artifact: {e.response.text}[/bold red]", title="[bold red]Error[/bold red]", border_style="red"))
    except Exception as e:
        console.print(Panel(f"[bold red]An unexpected error occurred: {e}[/bold red]", title="[bold red]Error[/bold red]", border_style="red"))
