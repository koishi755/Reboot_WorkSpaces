import json
import boto3

workspaces = boto3.client('workspaces')
workspaces_client_list = workspaces.describe_workspaces()

def lambda_handler(event, context):

    for workspaces_info in workspaces_client_list['Workspaces']:
        workspace_id = workspaces_info['WorkspaceId']
        workspace_state = workspaces_info['State']
    if workspace_state == 'UNHEALTHY':
        reboot_workspaces(workspace_id)

def reboot_workspaces(workspace_id):
    response = workspaces.reboot_workspaces(
        RebootWorkspaceRequests=[
            {
                'WorkspaceId': workspace_id
            },
        ]
    )