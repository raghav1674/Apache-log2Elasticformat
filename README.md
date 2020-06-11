
# Apache-Logs-2-Elastic-Search-Format




<img src="https://github.com/raghav1674/Apache-log2Elasticformat/blob/master/log-apache-task/at-present-access-log.PNG"/>
   


                                        HTTPD ACCESS_LOG FILE BEFORE CONVERSION TO JSON FORMAT
    
    
### APACHE-LOG 2 JSON

 
>python2 main.py -f <_log-file>
   
   
 <img src="https://github.com/raghav1674/Apache-log2Elasticformat/blob/master/log-apache-task/log-json-1.PNG"/>
    
                                                    CONVERTING TO  JSON FORMAT
    


### JSON 2 ELASTIC-SEARCH DOCUMENT FORMAT

 > python3 filter.py       <_json_converted_log_file>   <_type_name>  <output-file.json>
    
   
   <img src="https://github.com/raghav1674/Apache-log2Elasticformat/blob/master/log-apache-task/finally-converted.PNG"/>
    
    
                                            CONVERTING TO  ELASTIC-SEARCH DOCUMENT FORMAT
                                            
                                            
                                            
                                            
                                            
 #### BULK WRITE(PUT) TO THE ELASTICSEARCH INDEX 
 
 
 >curl -X PUT -H "Content-Type="apllication/json"  http://IP:9200/<INDEX>/_bulk  --data-binary  @<output-json-file(after running the above script)>
                                            
                                            
                                            
  <img src="https://github.com/raghav1674/Apache-log2Elasticformat/blob/master/log-apache-task/successful-put.PNG"/>                                    
                                            
                                            
 ####  QUERYING AND READING(GET) THROUGH SENSE AND  ELASTICSEARCH HEAD CHROME PLUGIN    
 
 
 
 
  <img src="https://github.com/raghav1674/Apache-log2Elasticformat/blob/master/log-apache-task/elastic_head_webui.PNG"/>
  
  
  
                                                  ELASTICSEARCH HEAD CHROME PLUGIN
                                                  
                                                  
  
  <img src="https://github.com/raghav1674/Apache-log2Elasticformat/blob/master/log-apache-task/sense-query-mozilla.PNG"/>
  
                                                        SENSE CHROME PLUGIN
 
                                            
    
