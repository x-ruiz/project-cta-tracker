package com.xavierruiz.models;

import java.util.List;

public class CtaData {
    private String tmst;
    private String errCd;
    private String errNm;
    private List<TrainData> eta;

    // Getters
    public String getTmst() {
        return tmst;
    }

    public String getErrCd() {
        return errCd;
    }

    public String getErrNm() {
        return errNm;
    }

    public List<TrainData> getEta() {
        return eta;
    }

    // Setters
    public void setTmst(String tmst) {
        this.tmst = tmst;
    }

    public void setErrCd(String errCd) {
        this.errCd = errCd;
    }

    public void setErrNm(String errNm) {
        this.errNm = errNm;
    }

    public void setEta(List<TrainData> eta) {
        this.eta = eta;
    }
}
