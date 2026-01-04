from utils.spark_utils import create_spark_session, read_from_s3, write_to_s3
from pyspark.sql.functions import col, count, sum as _sum
import logging
import sys


def main():
    spark = create_spark_session("Gold Transformation")

    try:
        # Read Silver data
        customer_df = read_from_s3(spark, "s3a://silver-bucket/customers/")
        account_df = read_from_s3(spark, "s3a://silver-bucket/accounts/")

        # -----------------------------
        # GOLD DIMENSION: dim_customers
        # -----------------------------
        dim_customers = (
            customer_df
            .select(
                col("customer_id"),
                col("full_name"),
                col("first_name"),
                col("last_name"),
                col("email"),
                col("country")
            )
            .dropDuplicates(["customer_id"])
        )

        # -----------------------------
        # GOLD FACT: fact_accounts
        # -----------------------------
        fact_accounts = (
            account_df
            .select(
                col("account_id"),
                col("customer_id"),
                col("account_type"),
                col("balance").cast("double"),
                col("status")
            )
        )

        # -----------------------------------
        # GOLD AGGREGATE: customer_account_summary
        # -----------------------------------
        customer_account_summary = (
            fact_accounts
            .groupBy("customer_id")
            .agg(
                count("account_id").alias("total_accounts"),
                _sum("balance").alias("total_balance")
            )
        )

        # -----------------------------
        # Write Gold outputs
        # -----------------------------
        write_to_s3(dim_customers, "s3a://gold-bucket/dim_customers/")
        write_to_s3(fact_accounts, "s3a://gold-bucket/fact_accounts/")
        write_to_s3(customer_account_summary, "s3a://gold-bucket/customer_account_summary/")

        logging.info("Gold transformation completed successfully")

    except Exception as e:
        logging.error(f"Gold transformation failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
