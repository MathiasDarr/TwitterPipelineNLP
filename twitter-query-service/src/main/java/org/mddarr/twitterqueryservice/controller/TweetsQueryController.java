package org.mddarr.twitterqueryservice.controller;


import org.elasticsearch.client.RestHighLevelClient;
import org.mddarr.twitterqueryservice.dto.TweetDTO;
import org.mddarr.twitterqueryservice.services.TweetsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;

@RestController
@RequestMapping(value = "/tweets/")
public class TweetsQueryController {
    @Autowired
    TweetsService tweetsService;

    @Autowired
    RestHighLevelClient highLevelClient;

    @GetMapping(value="get")
    @CrossOrigin
    public List<TweetDTO> get(@RequestParam(value="keyword") String keyword, @RequestParam(value="lat") Double lat,
                              @RequestParam(value="lng") Double lng) throws IOException {
        List<TweetDTO>response = this.tweetsService.searchTweetsByKeyword(this.highLevelClient, keyword, lat, lng);
        return response;
    }
}
