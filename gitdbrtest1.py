# Databricks notebook source
spark.conf.set("fs.azure.account.auth.type.gen2pc1.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.gen2pc1.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.gen2pc1.dfs.core.windows.net", "ea2dd659-9fe3-4741-af41-a55d58d4ca57")
spark.conf.set("fs.azure.account.oauth2.client.secret.gen2pc1.dfs.core.windows.net", "............" )
spark.conf.set("fs.azure.account.oauth2.client.endpoint.gen2pc1.dfs.core.windows.net", "https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47/oauth2/token")

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.gen2pc1.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.gen2pc1.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.gen2pc1.dfs.core.windows.net", "ea2dd659-9fe3-4741-af41-a55d58d4ca57")
spark.conf.set("fs.azure.account.oauth2.client.secret.gen2pc1.dfs.core.windows.net", "..................." )
spark.conf.set("fs.azure.account.oauth2.client.endpoint.gen2pc1.dfs.core.windows.net", "https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47/oauth2/token")

# COMMAND ----------

dbutils.fs.ls("abfss://dbrtest@gen2pc1.dfs.core.windows.net/")

# COMMAND ----------

# MAGIC %sh
# MAGIC nc -vz mssqlserverpc1.database.windows.net 1433

# COMMAND ----------

# MAGIC %sh
# MAGIC ping 

# COMMAND ----------

# MAGIC %sh
# MAGIC ping mssqlserverpc1.database.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -l /tmp

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -l /dbfs/databricks/tcpdump/0915-020629-7orf9snt

# COMMAND ----------

# MAGIC %sh
# MAGIC tcpdump -r /dbfs/databricks/tcpdump/0915-020629-7orf9snt/trace_2022_09_21_06_01_03#10.2.2.4.pcap

# COMMAND ----------

# MAGIC %sh
# MAGIC cp /dbfs/databricks/tcpdump/0915-020629-7orf9snt/trace_2022_09_21_06_01_03#10.2.2.4.pcap /dbfs/FileStore/trace_2022_09_21_06_01_03_10.2.2.4.pcap

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -l /dbfs/FileStore

# COMMAND ----------

# MAGIC %sh
# MAGIC tcpdump -r /tmp/trace_2022_09_21_05_56_03#10.2.2.4.pcap

# COMMAND ----------

# MAGIC %sh
# MAGIC tcpdump -r /dbfs/databricks/tcpdump/<cluster-id>/<node-ip>/trace-<timestamp>.pcap

# COMMAND ----------


dbutils.fs.mount(
 source = "wasbs://spark@blob1pc1.blob.core.windows.net/",
 mount_point = "/mnt/blob1pc1_spark",
 extra_configs = {"fs.azure.sas.spark.blob1pc1.blob.core.windows.net":"?sv=2019-10-10&si=spark-17E753E519A&sr=c&sig=MXA82CWMEPSnteLAO1HQthKyBClhieFwyAetN0QPNU4%3D"}
)

# COMMAND ----------



# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup arprodeastusa3.blob.core.windows.net
# MAGIC nslookup arprodeastusa6.blob.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /

# COMMAND ----------

dbutils.fs.mount(
 source = "wasbs://adf-source@blob1pc1.blob.core.windows.net",
 mount_point = "/mnt/adfsource",
 extra_configs = {"fs.azure.sas.adf-source.blob1pc1.blob.core.windows.net":"?sv=2019-10-10&st=2022-02-11T09%3A53%3A08Z&se=2022-02-11T10%3A10%3A00Z&sr=c&sp=rcwdl&sig=Qpxkw81nwDy4SnFTIC7Yp%2BPASXDqgAD71T45%2B5LprLU%3D"}
)

# COMMAND ----------

dbutils.fs.unmount("/mnt/adfsource")

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /dbfs/mnt/blob1pc1_spark

# COMMAND ----------

dbutils.fs.ls("dbfs:/mnt/blob1pc1_spark")

# COMMAND ----------

dbutils.fs.ls("dbfs:/mnt/adfsource")

# COMMAND ----------

dbutils.fs.mount(
 source = "wasbs://dbraccesstest@gen2pc1.blob.core.windows.net/",
 mount_point = "/mnt/test1",
 extra_configs = {"fs.azure.sas.dbraccesstest.gen2pc1.blob.core.windows.net":"?sv=2020-08-04&si=dbraccesstest-17E2EA9E&sig=zYtYUhXW21AtjXrxWLKNXj16qSG9F9kcIHRSbrK5YBc%3D"}
)

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -al /mnt

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -al /databricks/jars

# COMMAND ----------

dbutils.help()

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /dbfs/mnt/test

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /dbfs/mnt/test/mount.err

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

dbutils.fs.unmount("/mnt/gen2pc1")

# COMMAND ----------

# MAGIC %fs
# MAGIC ls dbfs:/mnt/gen2pc1

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

# MAGIC %sh
# MAGIC ping google.com

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup mic 

# COMMAND ----------

# MAGIC %sh
# MAGIC tcptraceroute dbartifactsprodeastus.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa1.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa2.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa3.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa4.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa5.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa6.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa7.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa8.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa9.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa10.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa11.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa12.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa13.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa14.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute arprodeastusa15.blob.core.windows.net 443
# MAGIC echo "===================="
# MAGIC tcptraceroute dbartifactsprodeastus2.blob.core.windows.net 443

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup dbstorage3urli4vfxvnka.blob.core.windows.net

# COMMAND ----------


