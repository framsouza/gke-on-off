from googleapiclient import discovery
from google.cloud import container_v1

client = container_v1.ClusterManagerClient()
zone = 'europe-west3-a'

def listproject():
    service = discovery.build('cloudresourcemanager', 'v1')
    request = service.projects().list()
    response = request.execute()

    for projects in response.get('projects', ['']):
        projectname = projects['projectId'].split(',')
        print("projectid:", projectname)

    return projectname

def listcluster():
    for project in listproject():
        clusterid = client.list_clusters(project_id=project, zone=zone)
        response = clusterid.clusters

        for clusters in response:
            clusterName = clusters.name
            print("clusterid:",clusterName)

    return clusterName

def listnodepools():
    for project in listproject():
        nodepools = client.list_node_pools(project_id=project, zone=zone, cluster_id=listcluster())
        response = nodepools.node_pools

        for nodes in response:
            pool = nodes.name
        print("nodepools:",pool)

    return pool
