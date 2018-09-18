Role Grafana
============

Grafana installer

Role Variables
--------------

Append datasources:

```yaml
grafana_datasources:
  - name: prometheus
    type: prometheus
    url: "http://localhost:9090"
```

Append dashboards from file:

```yaml
grafana_dashboards:
  - name: node_exporter
    file: dashboards/node_exporter.json
```

Example Playbook
----------------

    - hosts: servers
      roles:
        - role: sedovandrew.grafana
          grafana_datasources:
            - name: prometheus
              type: prometheus
              url: "http://localhost:9090"
          grafana_dashboards:
            - name: node_exporter
              file: dashboards/node_exporter.json

License
-------

BSD

Author Information
------------------

Sedov Andrey - sedoy80@gmail.com
