
docker run --name some-postgres -e POSTGRES_PASSWORD=postgres -d postgres
docker run --name some-app --link some-postgres:postgres -d application-that-uses-postgres