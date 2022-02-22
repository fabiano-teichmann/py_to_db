# Databricks notebook source

import os

import investpy

# COMMAND ---------- 
# MAGIC %run ./save_share/save_share
# COMMAND ---------- 
# COMMAND ---------- 
# MAGIC %run ./utils/logger
# COMMAND ---------- 


def get_list_share(country: str):
    # get list share and save in json
    list_share = investpy.get_stocks_list(country=country)
    save_share(list_share=list_share, country=country, path=os.environ["PATH_LIST_SHARE"])


if __name__ == "__main__":
    logger.info("Start get list share")
    get_list_share("brazil")
    logger.info("Finished")

# COMMAND ---------- 
