# Copilot-POC

### Purppose
To demonstrate deployment of simple 
- static html service
- flask app with postgres backend
- django with postgres backend

### Service(app) Directories
- **hello-copilot** is a service for simple static html service 
- **python** is a flask based service with postgres backend
- **django** is a django based service with postgres backend

**Note**: Postgres is not supported out-of-box by copilot , however it is supported as addon and, cloud formation config/template for same can be found under **addons** directory under respective service directory

### Deployment steps
- Set Aws profile<br>
```$expoert AWS_PROFILE=dev```
- Init App<br>
```copilot app init <app_name> --domain <domain_name> --resource-tags <key>=<value>``` 
- Init Environmnet<br>
```copilot env init --name <env_name> --container-insights --default-config```
- Deploy Environment<br>
```copilot env deploy --name <env_name>```
- Create Service secrets (needed for Django services)
    -  create secrets input file for python app <service_name>_secrets_input.yaml<br>
    ```
    DJANGO_SECRET_KEY:
        <env_name>: '<your secret key>'
    DJANGO_ALLOWED_HOSTS:
        <env_name>: '*'
    ```
    - Init Secrets<br>
    ```copilot init secret copilot secret init -a <app_name> --cli-input-yaml <service_name>_secret_input.yaml``` 
- Init Service<br>
```copilot svc init --name <service_name> --app <app_name> --svc-type "Load Balanced Web Service"``
- Deploy Service<br>
```copilot deploy --name <service_name> --app <app_name> --env <env_name>```

once service is deployed successfully , you should see a https link output of the form
```https://<service_name>.<env_name>.<app_name>.<domain_name>```

**Note:**
- We must supply domain if we want to use https connection
- service name needs to match service directory name
- Leave ALLOWED_HOSTS to '*' for PoC since it is easier to get done healthcheck that way.However,if you decide to use use specific hosts, you will neeed to figure out 
    - external domain of your service
    - internal ip of ALB running health check on service

