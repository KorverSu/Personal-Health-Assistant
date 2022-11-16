def postgres_sink(data_frame, table="dtable"):
    url = "jdbc:postgresql://database-1.caxexwzhx12d.ap-northeast-1.rds."
    properties = {
        "driver": "org.postgresql.Driver",
        "user": "postgres",
        "password": "postgres!"
    }

    data_frame.write.jdbc(url=url, table=table, mode="append",
                          properties=properties)


def foreach_batch_for_config(table="dtable"):
    def _(df, epoch_id):
        postgres_sink(data_frame=df, table=table)

    return _