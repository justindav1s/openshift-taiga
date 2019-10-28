# 1. Create new projects for the bc and dc 
NAMESPACE=$1
oc new-project ${NAMESPACE}

# 2. Run the builds for each components
# defaults are probs fine for standard build of latest stable branch
oc process -f templates/bc-taiga-back.yml | oc apply -n ${NAMESPACE} -f - 
oc start-build -n ${NAMESPACE} bc/taiga-back 

# 3. Deploy the images and config maps
# PostgreSQL db?
oc process -f templates/dc-postgresql-persistent.yml -p POSTGRESQL_USER=taiga -p POSTGRESQL_DATABASE=taiga -p VOLUME_CAPACITY=10Gi -p POSTGRESQL_VERSION=9.6 | oc apply -n ${NAMESPACE} -f -


# 4. Verify app is up by creating new admin user & password