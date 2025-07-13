package com.xavierruiz;

import com.google.gson.Gson;
import com.xavierruiz.models.CtaResponse;
import com.xavierruiz.models.CtaData;
import com.xavierruiz.utils.JsonUtils;

import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.types.Row;

public class Consumer {
    private static final Gson gson = new Gson();

    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // Source Set up
        KafkaSource<String> source = KafkaSource.<String>builder()
                .setBootstrapServers("localhost:9092")
                .setTopics("map-id-40380")
                .setGroupId("group-0")
                .setStartingOffsets(OffsetsInitializer.earliest())
                .setValueOnlyDeserializer(new SimpleStringSchema())
                .build();

        // Simple print as a sink
        // TrainData trainData = new TrainData();
        DataStream<Row> parsedStream = env.fromSource(source, WatermarkStrategy.noWatermarks(), "Kafka Source")
                .map(value -> {
                    // CtaData ctaData = JsonUtils.toJson(value, CtaData.class);
                    CtaResponse ctaResponse = JsonUtils.toJson(value, CtaResponse.class);
                    CtaData ctaData = ctaResponse.getCtatt();
                    return Row.of("value", 123);
                });

        env.execute("Flink Kafka Consumer");
    }
}
