package org.mddarr.twitterqueryservice.config;


import org.elasticsearch.client.RestHighLevelClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.elasticsearch.client.ClientConfiguration;
import org.springframework.data.elasticsearch.client.RestClients;
import org.springframework.data.elasticsearch.repository.config.EnableElasticsearchRepositories;

@Configuration
@EnableElasticsearchRepositories(basePackages = "org.mddarr.tweetsservice.dao")
@ComponentScan(basePackages = { "org.mddarr.tweetsservice" })
public class Config {
    @Bean
    RestHighLevelClient client() {

        ClientConfiguration clientConfiguration = ClientConfiguration.builder()
                .connectedTo("elasticsearch7:9200" ) //, "localhost:9200")
                .build();

        return RestClients.create(clientConfiguration).rest();
    }

}