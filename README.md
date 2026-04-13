# 🚀 Observability Project: Flask Monitoring with Prometheus & Grafana

## 📌 Overview

This project demonstrates how to implement observability for a Python Flask application using Prometheus and Grafana. It showcases metrics collection, monitoring, and visualization—key skills for DevOps and Site Reliability Engineering (SRE).

---

## 📂 Project Structure

```
OBSERVABILITY-PROJECT/
│
├── app/
│   ├── app.py               # Flask application with Prometheus metrics
│   ├── Dockerfile           # Docker configuration for the Flask app
│   └── requirements.txt     # Python dependencies
│
├── docker-compose.yaml      # Orchestrates all services
├── prometheus.yaml          # Prometheus configuration file
└── README.md                # Project documentation

#will be adding alerting soon
```

---

## 🛠️ Tech Stack

* **Python (Flask)** – Web Application
* **Prometheus** – Metrics Collection
* **Grafana** – Metrics Visualization
* **Docker & Docker Compose** – Containerization
* **cAdvisor** – Docker Container Monitoring
* **PromQL** – Querying Metrics

---

## 📊 Application Metrics

The Flask app exposes metrics at the `/metrics` endpoint using the Prometheus client library.

### Custom Metric

| Metric Name           | Description                                        |
| --------------------- | -------------------------------------------------- |
| `my_app_visits_total` | Tracks the total number of visits to the home page |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/observability-project.git
cd observability-project
```

### 2️⃣ Run the Project

Start all services using Docker Compose:

```bash
docker-compose up --build
```

To run in detached mode:

```bash
docker-compose up -d --build
```

---

## 🌐 Access the Services

| Service           | URL                           |
| ----------------- | ----------------------------- |
| Flask Application | http://localhost:5225         |
| Flask Metrics     | http://localhost:5225/metrics |
| Prometheus        | http://localhost:9090         |
| Grafana           | http://localhost:3000         |
| cAdvisor          | http://localhost:8080         |

### Grafana Login Credentials

* **Username:** `admin`
* **Password:** `admin`

---

## ⚙️ Configure Grafana

1. Open Grafana at **http://localhost:3000**.
2. Navigate to **Connections → Data Sources**.
3. Add a **Prometheus** data source.
4. Set the URL to:

   ```
   http://prometheus:9090
   ```
5. Click **Save & Test**.
6. Import your dashboard JSON.

---

## 📈 Useful Prometheus Queries

| Description                  | Query                                        |
| ---------------------------- | -------------------------------------------- |
| Total Visits                 | `my_app_visits_total`                        |
| Total Visits (All Instances) | `sum(my_app_visits_total{job="python_app"})` |
| Requests Per Second          | `rate(my_app_visits_total[1m])`              |
| Requests Per Minute          | `rate(my_app_visits_total[1m]) * 60`         |
| Visits in Last 5 Minutes     | `increase(my_app_visits_total[5m])`          |
| Application Health           | `up{job="python_app"}`                       |

---

## 🧪 Generate Sample Traffic

```bash
for i in {1..50}; do curl http://localhost:5225/; done
```

Verify metrics:

```bash
curl http://localhost:5225/metrics
```

---

## 🎯 Skills Demonstrated

* Observability and Monitoring
* Prometheus & PromQL
* Grafana Dashboarding
* Docker & Container Monitoring
* Python Flask Development
* Site Reliability Engineering (SRE)
* Infrastructure as Code

---

## 🔮 Future Enhancements

* Add Alertmanager for notifications - inprogress
* Deploy on Kubernetes
* Integrate GitHub Actions for CI/CD
* Add OpenTelemetry for distributed tracing
* Deploy on AWS (EKS/EC2)

---

## 👨‍💻 Author

**Abishek K V**
Site Reliability Engineer | Observability | DevOps | Cloud Enthusiast

* GitHub: https://github.com/happieshake
* LinkedIn: www.linkedin.com/in/abishek-kv

