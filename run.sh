# 1. Create new projects for the bc and dc 
NAMESPACE=$1
oc new-project ${NAMESPACE}

# 2. Run the builds for each components
# defaults are probs fine for standard build of latest stable branch
oc process -f templates/bc-taiga-back.yml \
    | oc apply -n ${NAMESPACE} -f - 
oc start-build -n ${NAMESPACE} bc/taiga-back

# 3. Deploy the images and config maps
# PostgreSQL db?
oc process -f templates/dc-postgresql-persistent.yml \
    -p POSTGRESQL_USER=taiga \
    -p POSTGRESQL_DATABASE=taiga \
    -p VOLUME_CAPACITY=10Gi \
    -p POSTGRESQL_VERSION=9.6 \
    | oc apply -n ${NAMESPACE} -f -

oc process -f templates/dc-taiga-back.yml \
    -p IMAGESTREAM_NAMESPACE=${NAMESPACE} \
    -p TAIGA_FRONT_DOMAIN=taiga-${NAMESPACE}.apps.forumeu.emea-1.rht-labs.com \
    -p TAIGA_BACK_DOMAIN=taiga-back-${NAMESPACE}.apps.forumeu.emea-1.rht-labs.com \
    -p PUBLIC_REGISTER_ENABLED=true \
    | oc apply -n ${NAMESPACE} -f -


# 4. Verify app is up by creating new admin user & password
