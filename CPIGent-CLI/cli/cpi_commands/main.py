import typer
from cli.cpi_commands.packages import list_packages
from cli.cpi_commands.artifacts import list_artifacts, download_artifact, deploy_artifact

cpi_app = typer.Typer()
list_commands_app = typer.Typer(help="Commands for listing CPI entities.")

@list_commands_app.command("packages")
def packages():
    list_packages()

@list_commands_app.command("artifacts")
def artifacts():
    list_artifacts()

cpi_app.add_typer(list_commands_app, name="list")

@cpi_app.command("download")
def download(
    artifact_id: str = typer.Argument(..., help="The ID of the artifact to download."),
    version: str = typer.Option("active", help="The version of the artifact to download.")
):
    """Downloads a specific integration artifact by its ID."""
    download_artifact(artifact_id, version)

@cpi_app.command("deploy")
def deploy(
    file_path: str = typer.Argument(..., help="The path to the artifact file to deploy."),
    artifact_id: str = typer.Option(..., help="The ID of the artifact."),
    artifact_name: str = typer.Option(..., help="The name of the artifact."),
    package_id: str = typer.Option(..., help="The ID of the package to deploy to.")
):
    """Deploys an integration artifact (iFlow) to SAP CPI."""
    deploy_artifact(file_path, artifact_id, artifact_name, package_id)
