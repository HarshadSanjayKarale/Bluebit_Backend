workers = 2  # Reduce from 4 to 2
threads = 2
timeout = 60
bind = "0.0.0.0:5000"
max_requests = 500
max_requests_jitter = 100
worker_class = 'gthread'
preload_app = False  # Don't preload the app to save memory