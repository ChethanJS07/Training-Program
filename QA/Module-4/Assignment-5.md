## Assignment 5 – JMeter Test Analysis

### Scenario

After running a JMeter test:

| Metric                | Result      |
| --------------------- | ----------- |
| Users                 | 500         |
| Average Response Time | 4.5 sec     |
| Throughput            | 120 req/sec |
| Error Rate            | 12%         |

**Customer Requirements:**

- Response Time < 2 sec
- Error Rate < 1%

---

### 1. Is the application meeting customer requirements?

**No.**

- Response Time: **4.5 sec** (required: < 2 sec) – **FAIL**
- Error Rate: **12%** (required: < 1%) – **FAIL**

The application is **not** meeting the customer requirements.

---

### 2. Which metrics indicate a problem?

| Metric                              | Problem?               | Why                                                                                                                                                           |
| ----------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Average Response Time (4.5 sec)** | Yes                    | More than double the acceptable limit (2 sec). Indicates the system is slow under load.                                                                       |
| **Error Rate (12%)**                | Yes                    | Exceeds the 1% threshold. Suggests the system is failing many requests (timeouts, server errors, DB connection failures).                                     |
| **Throughput (120 req/sec)**        | Not directly a problem | Throughput of 120 req/sec might be acceptable for the system's capacity, but it's questionable because many requests are failing and response times are high. |

---

### 3. Suggest possible causes

| Cause                                   | Explanation                                                                                                                                     |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Backend overload**                    | The server (app server, database, or external API) cannot handle 500 concurrent users. CPU/memory or connection pool limits are being exceeded. |
| **Database bottleneck**                 | Slow queries, missing indexes, or lock contention cause high response times.                                                                    |
| **Network latency / bandwidth**         | If the test is executed from a different location, network delays could contribute. However, this is unlikely to cause 12% errors.              |
| **Application code issues**             | Inefficient algorithms, synchronous blocking calls, or unoptimized endpoints.                                                                   |
| **Resource limits**                     | Server may be hitting max connections, file descriptors, or thread pool limits, leading to timeouts and errors.                                 |
| **Load balancer / firewall throttling** | Rate limiting or firewall rules may be dropping or delaying requests.                                                                           |

---

### 4. Recommend the next steps

| Step | Action                                                                                                                                                        |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | **Analyze server-side logs** – Check application, database, and web server logs for errors, slow queries, or timeouts during the test.                        |
| 2    | **Monitor server resources** – Use monitoring tools (e.g., top, htop, Grafana, CloudWatch) to check CPU, memory, disk I/O, and network usage during the test. |
| 3    | **Check database performance** – Enable slow query logging and analyse execution plans. Consider adding indexes or optimizing queries.                        |
| 4    | **Increase server resources** – If CPU/memory is maxed out, scale up (larger instance) or scale out (add more instances with a load balancer).                |
| 5    | **Add caching** – Implement caching for frequently accessed data (Redis, Memcached) to reduce backend load.                                                   |
| 6    | **Tune connection pools** – Increase max connections in the app server and database pool settings.                                                            |
| 7    | **Implement retry logic** – For transient errors (e.g., network timeouts), add retry mechanisms on the client side.                                           |
| 8    | **Re-run the test** – After applying fixes, run the same JMeter test and compare results.                                                                     |

---
