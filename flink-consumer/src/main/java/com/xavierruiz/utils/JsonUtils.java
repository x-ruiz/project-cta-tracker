package com.xavierruiz.utils;

import com.google.gson.Gson;

public class JsonUtils {
    private static final Gson gson = new Gson();

    public static <T> T toJson(String json, Class<T> object) {
        return gson.fromJson(json, object);
    }
}