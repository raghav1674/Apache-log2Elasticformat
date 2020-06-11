
# Apache-Logs-2-Elastic-Search-Format




<img src="https://github.com/raghav1674/Apache-log2Elasticformat/blob/master/log-apache-task/at-present-access-log.PNG"/>
   


                                        HTTPD ACCESS_LOG FILE BEFORE CONVERSION TO JSON FORMAT
    
    
### APACHE-LOG 2 JSON

 
>python2 main.py -f <log-file>
   
   
 <img src="https://github.com/raghav1674/Apache-log2Elasticformat/blob/master/log-apache-task/log-json-1.PNG"/>
    
                                                    CONVERTING TO  JSON FORMAT
    


### JSON 2 ELASTIC-SEARCH DOCUMENT FORMAT

 >python3 filter.py <json-converted-log-file>   <_type-name>  <output-file.json>
    
   
   <img src="https://github.com/raghav1674/Apache-log2Elasticformat/blob/master/log-apache-task/finally-converted.PNG"/>
    
    
                                            CONVERTING TO  ELASTIC-SEARCH DOCUMENT FORMAT
                                            
                                            
                                            
                                            
 ####  QUERYING AND READING(GET) THROUGH SENSE AND  ELASTICSEARCH HEAD CHROME PLUGIN    
 
 
 
 
  <img src="https://github.com/raghav1674/Apache-log2Elasticformat/blob/master/log-apache-task/finally-converted.PNG"/>
 
                                            
    
