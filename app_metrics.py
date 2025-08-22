from diagrams import Cluster, Diagram
from diagrams.gcp.operations import Monitoring
from diagrams.oci.connectivity import Backbone
from diagrams.onprem.database import InfluxDB
from diagrams.onprem.queue import Kafka
from diagrams.programming.flowchart import MultipleDocuments
from diagrams.programming.language import Python
from diagrams.saas.chat import Slack

graph_attr = {
    "label": "",
    "labelloc": "ttc",
    "nodesep": "0.2",
    "pad": "0.2",
    "ranksep": "0.75",
    "splines": "spline",
}

node_attr = {
    "fontsize": "12.0",
}

with Diagram(
    "Starting point",
    show=False,
    filename="app_metrics",
    outformat="png",
    graph_attr=graph_attr,
    node_attr=node_attr,
):
    with Cluster("Phalanx Kubernetes cluster"):
        with Cluster("Your app"):
            application = Python("Metrics")

        with Cluster("Sasquatch"):
            topic = Kafka("Kafka")
            schema_manager = MultipleDocuments("Schema Manager")
            telegraf = Backbone("Telegraf")
            influxdb = InfluxDB("InfluxDB v1")
            chronograf = Monitoring("Chronograf")

    slack = Slack("Slack alerts")

    application >> topic >> telegraf >> influxdb
    slack << chronograf >> influxdb
    application >> schema_manager
    telegraf >> schema_manager
