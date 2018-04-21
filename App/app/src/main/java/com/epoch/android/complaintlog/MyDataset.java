package com.epoch.android.complaintlog;

import com.android.volley.toolbox.StringRequest;

import java.io.Serializable;

/**
 * Created by dell on 29-Mar-18.
 */

public class MyDataset implements Serializable{

    private Boolean resolved;
    private String trainNum;
    private String complaintLink;
    private String query;
    private String pts;
    public int complaintId;
    private String trainName;
    private String station;
    private String seatNo;
    private String complaintDept;
    private Boolean newComplaint;
    private String email;
    private String time;

    /*
    "resolved": false,
    "train-no": null,
    "link": "sdadas",
    "query": "0",
    "pts": "12569",
    "id": 1,
    "train-name": null,
    "station": "Vadodara",
    "seat-no": "s2",
    "department": "money",
    "new": true,
    "email": "adasda"
     */

    public MyDataset(Boolean resolved, String trainNum, String complaintLink, String query, String pts, int complaintId, String trainName, String station, String seatNo, String complaintDept, Boolean newComplaint, String email, String time) {
        this.resolved = resolved;
        this.trainNum = trainNum;
        this.complaintLink = complaintLink;
        this.query = query;
        this.pts = pts;
        this.complaintId = complaintId;
        this.trainName = trainName;
        this.station = station;
        this.seatNo = seatNo;
        this.complaintDept = complaintDept;
        this.newComplaint = newComplaint;
        this.email = email;
        this.time = time;
        if (time.isEmpty()) {
            time = "HH:MM";
        }
    }

    public int getComplaintId() {
        return complaintId;
    }

    public String getComplaintDept() {
        return complaintDept;
    }

    public String getQuery() {
        return query;
    }

    public String getEmail() {
        return email;
    }

    public String getPts() {
        return pts;
    }

    public String getTrainNum() {
        return trainNum;
    }

    public String getTrainName() {
        return trainName;
    }

    public String getSeatNo() {
        return seatNo;
    }

    public String getStation() {
        return station;
    }

    public String getComplaintLink() {
        return complaintLink;
    }

    public Boolean getResolved() {
        return resolved;
    }

    public Boolean getNewComplaint() {
        return newComplaint;
    }

    public String getTime() {
        return time;
    }

    public String getComplaintIdString(){
        return "Complaint #" + complaintId;
    }

    @Override
    public String toString() {
        return super.toString();
    }
}
