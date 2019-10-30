# 1. Create new projects for the bc and dc 

NAMESPACE=${2:-"labs-pm"}
CLUSTER_DOMAIN=${1}
if [ -z "${1}" ];then echo "Please set the cluster url eg apps.mydomain.location.example.com"; exit 1;fi

echo "\n Creating new project ${NAMESPACE} and setting it"
oc new-project ${NAMESPACE}
oc project ${NAMESPACE}

# 2. Run the builds for each components
# defaults are probs fine for standard build of latest stable branch
echo "\n Running build for Taiga Backend "
oc process -f templates/bc-taiga-back.yml \
    | oc apply -n ${NAMESPACE} -f - 
oc start-build -n ${NAMESPACE} bc/taiga-back

echo "\n Running build for Taiga frontend "
oc process -f templates/bc-taiga-front.yml \
    | oc apply -n ds-test -f -
oc start-build -n ${NAMESPACE} bc/taiga-front

# 3. Deploy the images and config maps
# PostgreSQL db?
echo "\n Deploying PostgreSQL for Taiga Backend"
oc process -f templates/dc-postgresql-persistent.yml \
    -p POSTGRESQL_USER=taiga \
    -p POSTGRESQL_DATABASE=taiga \
    -p VOLUME_CAPACITY=10Gi \
    -p POSTGRESQL_VERSION=10 \
    | oc apply -n ${NAMESPACE} -f -

echo "\n Deploying Taiga Backend"
oc process -f templates/dc-taiga-back.yml \
    -p NAMESPACE=${NAMESPACE} \
    -p TAIGA_FRONT_DOMAIN=taiga-${NAMESPACE}.apps.forumeu.emea-1.rht-labs.com \
    -p TAIGA_BACK_DOMAIN=taiga-back-${NAMESPACE}.apps.forumeu.emea-1.rht-labs.com \
    -p PUBLIC_REGISTER_ENABLED=true \
    | oc apply -n ${NAMESPACE} -f -

echo "\n Deploying Taiga Frontend"
oc process -f templates/dc-taiga-front.yml \
    -p NAME=taiga-front \
    -p ROUTE_PATH=taiga \
    -p NAMESPACE=${NAMESPACE} \
    -p TAIGA_BACKEND_URL=https://taiga-back-${NAMESPACE}.apps.forumeu.emea-1.rht-labs.com \
    -p PUBLIC_REGISTER_ENABLED=true \
    -p ENV_MOUNT_PATH="/opt/app-root/src/settings/" \
    | oc apply -n ${NAMESPACE} -f -

# 4. Verify app is up by creating new admin user & password
