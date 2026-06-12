from robusta.api import *

@action
def grafana_timed_panel_button(alert: PrometheusKubernetesAlert):
    labels      = alert.alert.labels
    dash_uid    = labels.get("dashboard_uid", "")
    panel_id    = labels.get("panel_id", "")
    cluster     = labels.get("cluster", "")
    runbook_url = labels.get("runbook_url", "")

    if not dash_uid:
        return

    starts_at   = alert.alert.starts_at
    from_ms     = int((starts_at.timestamp() - 900)  * 1000)
    to_ms       = int((starts_at.timestamp() + 3600) * 1000)

    base   = f"https://grafana.prophetx.dev/d/{dash_uid}"
    params = f"orgId=1&var-cluster={cluster}&var-currency=cash&from={from_ms}&to={to_ms}"

    alert.add_enrichment([ButtonBlock("📊 Dashboard", f"{base}?{params}")])
    if panel_id:
        alert.add_enrichment([ButtonBlock("📈 Panel", f"{base}?{params}&viewPanel={panel_id}")])
    if runbook_url:
        alert.add_enrichment([ButtonBlock("📖 Runbook", runbook_url)])
