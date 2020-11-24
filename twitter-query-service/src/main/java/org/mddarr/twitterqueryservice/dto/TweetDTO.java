package org.mddarr.twitterqueryservice.dto;

public class TweetDTO {
    String screename;
    String name;
    String tweet_content;
    String location;
    Long tweet_time;
    Long id;
    Double lat;
    Double lng;

    @Override
    public String toString() {
        return "TweetDTO{" +
                "screename='" + screename + '\'' +
                ", name='" + name + '\'' +
                ", tweet_content='" + tweet_content + '\'' +
                ", location='" + location + '\'' +
                ", tweet_time=" + tweet_time +
                ", id=" + id +
                '}';
    }

}
