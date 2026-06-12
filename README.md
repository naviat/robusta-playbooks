# How to use
In robusta_values_*.yaml helm value:

```yaml
# base values.yaml
playbookRepos:
  - url: "https://github.com/naviat/robusta-playbooks.git"
    playbooks_root_path: "custom_actions"
```

And replace `TradeAlertButtons` actions with - `grafana_timed_panel_button: {}`.
