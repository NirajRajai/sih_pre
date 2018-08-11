package com.epoch.android.complaintlog;

import android.app.Activity;
import android.app.Dialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.NavUtils;
import android.support.v7.app.AlertDialog;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.app.ActionBar;
import android.view.MenuItem;
import android.util.Log;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

/**
 * An activity representing a single Item detail screen. This
 * activity is only used on narrow width devices. On tablet-size devices,
 * item details are presented side-by-side with a list of items
 * in a {@link ItemListActivity}.
 */
public class ItemDetailActivity extends AppCompatActivity {

    private static final String TAG = "ItemDetailActivity";

    public static final String HOST = "http://192.168.43.52:5000";

    private TextView textViewComplaintId;
    private TextView textViewComplaint;
    private TextView textViewTime;
    private Button buttonMarkResolved;
    private Spinner spinnerForward;
    private static final String URL_RESOLVED = HOST+"/cappshaw?id=";
    private static final String URL_READ = HOST+"/cappmark?id=";
    private static final String URL_FORWARD = HOST+"/cappresolve?id="; //department=
    Activity activity = new Activity();
    private TextView textViewStation;
    private TextView textViewTrainNo;
    private TextView textViewLink;
    ArrayList<String > forwardList = new ArrayList<String >();
    String colors[] = {"Forward to:", "cleanliness", "booking", "electric", "irctc_care", "irctc_staff", "late", "medical", "none", "security", "staff", "water"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.complaint_view_full);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar_full);
        setSupportActionBar(toolbar);
        Log.d(TAG, "onCreate: "+TAG);



        Bundle bundle = getIntent().getExtras();
        final MyDataset item = (MyDataset) getIntent().getSerializableExtra("MyDataset");

        textViewComplaint = findViewById(R.id.complaint_text_full);
        textViewTime = findViewById(R.id.complaint_time_full);
        textViewComplaintId = findViewById(R.id.complaint_id_full);
        textViewStation = findViewById(R.id.text_view_station);
        textViewTrainNo = findViewById(R.id.text_view_train_no);
        textViewLink = findViewById(R.id.text_view_link);

        textViewComplaint.setText(item.getQuery());
        textViewComplaintId.setText(item.getComplaintIdString());
        textViewTime.setText(item.getTime());
        textViewStation.setText(item.getStation());
        String holder = item.getTrainNum()+"/"+item.getTrainName();
        textViewTrainNo.setText(holder);
        textViewLink.setText(item.getComplaintLink());
        buttonMarkResolved = findViewById(R.id.button_mark_resolved);
        spinnerForward = findViewById(R.id.spinner);

        callApi(URL_READ+item.getComplaintId());

//        getForwardList(URL_FORWARD);

        ArrayAdapter<String> spinnerArrayAdapter = new ArrayAdapter<String>(this,   android.R.layout.simple_spinner_item, colors);
        spinnerArrayAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item); // The drop down view
        spinnerForward.setAdapter(spinnerArrayAdapter);


        spinnerForward.setAdapter(spinnerArrayAdapter);



        spinnerForward.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, final int i, long l) {
                if(i>0){
                    final AlertDialog.Builder builder = new AlertDialog.Builder(ItemDetailActivity.this);
                    builder.setMessage("Forward complaint to " + colors[i] + "?");

                    builder.setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int id) {
                            // User clicked OK button
                            callApi(URL_FORWARD+ item.getComplaintId() + "&department="+colors[i]);
                            Toast.makeText(ItemDetailActivity.this, "Forwarding to " + colors[i] + "...", Toast.LENGTH_SHORT).show();
                            NavUtils.navigateUpFromSameTask(ItemDetailActivity.this);
                        }
                    });
                    builder.setNegativeButton("Not yet", new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int id) {
                            // User cancelled the dialog
                        }
                    });
                    AlertDialog dialog = builder.create();
                    dialog.show();
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        buttonMarkResolved.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//                Context context = view.getContext();
//                Intent intent = new Intent(context, ItemListActivity.class);
//                    intent.putExtra(ItemDetailFragment.ARG_ITEM_ID, item.getComplaintIdString(
//                NavUtils.navigateUpFromSameTask(ItemDetailActivity.this);
                final AlertDialog.Builder builder = new AlertDialog.Builder(ItemDetailActivity.this);
                builder.setMessage("Close the complaint?");

                builder.setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        // User clicked OK button
                        callApi(URL_RESOLVED+item.getComplaintId());
                        NavUtils.navigateUpFromSameTask(ItemDetailActivity.this);

                    }
                });
                builder.setNegativeButton("Not yet", new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        // User cancelled the dialog
                    }
                });
                AlertDialog dialog = builder.create();
                dialog.show();
            }
        });


//        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
//        fab.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Snackbar.make(view, "Replace with your own detail action", Snackbar.LENGTH_LONG)
//                        .setAction("Action", null).show();
//            }
//        });

        // Show the Up button in the action bar.
        ActionBar actionBar = getSupportActionBar();
        if (actionBar != null) {
            actionBar.setDisplayHomeAsUpEnabled(true);
        }

        // savedInstanceState is non-null when there is fragment state
        // saved from previous configurations of this activity
        // (e.g. when rotating the screen from portrait to landscape).
        // In this case, the fragment will automatically be re-added
        // to its container so we don't need to manually add it.
        // For more information, see the Fragments API guide at:
        //
        // http://developer.android.com/guide/components/fragments.html
        //
//        if (savedInstanceState == null) {
//            // Create the detail fragment and add it to the activity
//            // using a fragment transaction.
//            Bundle arguments = new Bundle();
//            arguments.putString(ItemDetailFragment.ARG_ITEM_ID,
//                    getIntent().getStringExtra(ItemDetailFragment.ARG_ITEM_ID));
//            ItemDetailFragment fragment = new ItemDetailFragment();
//            fragment.setArguments(arguments);
//            getSupportFragmentManager().beginTransaction()
//                    .add(R.id.item_detail_container, fragment)
//                    .commit();
//        }
    }

    private void getForwardList(String URL) {
        StringRequest stringRequest = new StringRequest(Request.Method.GET, URL,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

//                        try {
//                            ArrayList<String> forwardList = new ArrayList<String>();
//                            forwardList.add("Forward to:");
//                            JSONObject jsonObject = new JSONObject(response);
//                            JSONArray jsonArray = jsonObject.getJSONArray("complaints");
//
//                            for(int i=0; i<jsonArray.length(); i++) {
//                                JSONObject jsonComplaint = jsonArray.getJSONObject(i);
//                                MyDataset item = new MyDataset(
//                                        jsonComplaint.getInt("id"),
//                                        jsonComplaint.getString("dept"),
//                                        jsonComplaint.getString("query"),
//                                        jsonComplaint.getString("email"),
//                                        jsonComplaint.getString("pts"),
//                                        jsonComplaint.getString("train-no"),
//                                        jsonComplaint.getString("train-name"),
//                                        jsonComplaint.getString("seat-no"),
//                                        jsonComplaint.getString("station"),
//                                        jsonComplaint.getString("link"),
//                                        jsonComplaint.getInt("resolved"),
//                                        jsonComplaint.getInt("new"),
//                                        jsonComplaint.getString("time")
//                                );
//                                listItems.add(item);
//                            forwardList.add(item);
//                        } catch (JSONException e) {
//                            e.printStackTrace();
//                        }


                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

            }
        });

        RequestQueue requestQueue = Volley.newRequestQueue(this);
        requestQueue.add(stringRequest);
    }

    private void callApi(String URL) {
        StringRequest stringRequest = new StringRequest(Request.Method.GET, URL,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

            }
        });

        RequestQueue requestQueue = Volley.newRequestQueue(this);
        requestQueue.add(stringRequest);
    }

//    @Override
//    public boolean onOptionsItemSelected(MenuItem item) {
//        int id = item.getItemId();
//        if (id == android.R.id.home) {
//            // This ID represents the Home or Up button. In the case of this
//            // activity, the Up button is shown. For
//            // more details, see the Navigation pattern on Android Design:
//            //
//            // http://developer.android.com/design/patterns/navigation.html#up-vs-back
//            //
//            navigateUpTo(new Intent(this, ItemListActivity.class));
//            return true;
//        }
//        return super.onOptionsItemSelected(item);
//    }
}
