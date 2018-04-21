package com.epoch.android.complaintlog;

import android.app.LauncherActivity;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.annotation.NonNull;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.DefaultItemAnimator;
import android.support.v7.widget.DividerItemDecoration;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;


import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.epoch.android.complaintlog.dummy.DummyContent;
import com.twitter.sdk.android.core.Twitter;

import java.util.ArrayList;
import java.util.List;
import com.epoch.android.complaintlog.MyDataset;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;


class Temp{
    int i;

    public Temp(int i) {
        this.i = i;
    }
}

public class ItemListActivity extends AppCompatActivity {

    private static final String HOST = "http://192.168.43.52:5000";
    //resolved:  cappallresolve?department=
    private static final String TAG = "ItemListActivity";
    private boolean mTwoPane;
    private LinearLayoutManager mLayoutManager;
    RecyclerView.Adapter mAdapter;
    private List<MyDataset> listItems;
    Context acticityContext = this;
    private DrawerLayout mDrawerLayout;
    String username;

    final String URL_CREATE = HOST+"/cappcreate?created=True&department=";
    final String URL_RES = HOST+"/cappallresolve?department=";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Log.d(TAG, "onCreate: ItemListActivity started");
        username = getIntent().getStringExtra("username");
        Log.d(TAG, "onCreate: username="+username);



        Log.d(TAG, "onCreate: called oncreate from start");
//        Twitter.initialize(this);

        setContentView(R.layout.activity_item_list);

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar_small);
        setSupportActionBar(toolbar);
        Log.d(TAG, "onCreate: toolbar binded");
        try{
            ActionBar actionbar = getSupportActionBar();
            actionbar.setDisplayHomeAsUpEnabled(true);
            actionbar.setHomeAsUpIndicator(R.drawable.ic_menu_black_24dp);
        }catch (Exception e){
            Log.e(TAG, "onCreate: "+ e.getMessage() );
        }

        Log.d(TAG, "onCreate: action bar binded");
//
//        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
//        fab.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
//                        .setAction("Action", null).show();
//            }
//        });

        if (findViewById(R.id.item_detail_container) != null) {
            // The detail container view will be present only in the
            // large-screen layouts (res/values-w900dp).
            // If this view is present, then the
            // activity should be in two-pane mode.
            mTwoPane = true;
        }

        mDrawerLayout = findViewById(R.id.drawer_layout);

        NavigationView navigationView = findViewById(R.id.nav_view);
        navigationView.getMenu().getItem(0).setChecked(true);

        navigationView.setNavigationItemSelectedListener(
                new NavigationView.OnNavigationItemSelectedListener() {
                    @Override
                    public boolean onNavigationItemSelected(MenuItem menuItem) {
                        // set item as selected to persist highlight
                        menuItem.setChecked(true);
                        // close drawer when item is tapped
                        mDrawerLayout.closeDrawers();

                        if(menuItem.getItemId() == R.id.open_complaints){
//                            listItems.clear();
                            mDrawerLayout.closeDrawers();
                            refreshRecyclerViewData(username);
                        } else if (menuItem.getItemId() == R.id.resolved_complaints){
//                            listItems.clear();
                            mDrawerLayout.closeDrawers();
                            refreshRecyclerViewDataRes(username);
//                            Intent intent = new Intent(ItemListActivity.this, ResolvedItemListActivity.java);
                        }
                        // Add code here to update the UI based on the item selected
                        // For example, swap UI fragments here

                        return true;
                    }
                });

        RecyclerView recyclerView = findViewById(R.id.item_list);
        recyclerView.setHasFixedSize(true);
//        assert recyclerView != null;
        mLayoutManager = new LinearLayoutManager(this);
        recyclerView.setLayoutManager(mLayoutManager);

        DividerItemDecoration dividerItemDecoration = new DividerItemDecoration(recyclerView.getContext(),
                mLayoutManager.getOrientation());
        recyclerView.addItemDecoration(dividerItemDecoration);

        listItems = new ArrayList<>();

        loadRecyclerViewData(URL_CREATE + username);

        Log.d(TAG, "onCreate: return form loadRecyclerViewData");

//        for (int i=0; i<=10; i++) {
//            MyDataset listItem = new MyDataset(
//                    i,
//                    "Complaint Dept",
//                    "Complaint Complaint Complaint " + i,
//                    "example@google.com",
//                    "pts" + i,
//                    "1200" + i,
//                    "Train Name: " + i,
//                    "S/0" + i,
//                    "Station: " + i,
//                    "temp.link/" + i,
//                    0,
//                    1,
//                    "HH:MM"
//            );
//
//            listItems.add(listItem);
//        }


//        mAdapter = new SimpleItemRecyclerViewAdapter(this, mTwoPane, this, listItems);
//        recyclerView.setAdapter(mAdapter);
//        setupRecyclerView(recyclerView);
//        mAdapter = new MyAdapter(myDataset);
//        recyclerView.setAdapter(mAdapter);

     //   loadRecyclerViewData(URL_CREATE);
        mAdapter = new SimpleItemRecyclerViewAdapter(this, mTwoPane, this, listItems);
        recyclerView.setAdapter(mAdapter);
        RecyclerView.ItemAnimator itemAnimator = new DefaultItemAnimator();
        recyclerView.setItemAnimator(itemAnimator);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case android.R.id.home:
                mDrawerLayout.openDrawer(GravityCompat.START);
                return true;
            case R.id.refresh:
                listItems.clear();
                refreshRecyclerViewData(URL_CREATE + username);

                return true;
        }
        return super.onOptionsItemSelected(item);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.actionbar, menu);
        return true;
    }
//    private void setupRecyclerView(@NonNull RecyclerView recyclerView) {
//        recyclerView.setAdapter(new SimpleItemRecyclerViewAdapter(this, DummyContent.ITEMS, mTwoPane));
//    }


    private void refreshRecyclerViewDataRes(String username) {
        loadRecyclerViewData(URL_RES + username);
        mAdapter.notifyDataSetChanged();
    }

    private void refreshRecyclerViewData(String username) {
        loadRecyclerViewData(URL_CREATE + username);
        mAdapter.notifyDataSetChanged();
    }


    private void loadRecyclerViewData(String URL_CREATE) {

        Log.d(TAG, "loadRecyclerViewData: making network call");
        final ProgressDialog progressDialog = new ProgressDialog(this);
        progressDialog.setMessage("Loading Complaints");
        progressDialog.show();

        StringRequest stringRequest = new StringRequest(Request.Method.GET, URL_CREATE,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        try {
                            JSONArray jsonArray = new JSONArray(response);
                            Log.d(TAG, "onResponse: JSON:" + jsonArray);
                            Log.d(TAG, "onResponse: jsonArray.length()="+jsonArray.length());
                            for(int i=0; i<jsonArray.length(); i++) {
                                Log.d(TAG, "onResponse: enter for loop");
                                JSONObject jsonComplaint = jsonArray.getJSONObject(i);
                                Log.d(TAG, "onResponse: jsonComplaint: "+jsonComplaint);

//                                /*
                                MyDataset item = new MyDataset(
                                        jsonComplaint.getBoolean("resolved"),
                                        jsonComplaint.getString("train-no"),
                                        jsonComplaint.getString("link"),
                                        jsonComplaint.getString("query"),
                                        jsonComplaint.getString("pts"),
                                        jsonComplaint.getInt("id"),
                                        jsonComplaint.getString("train-name"),
                                        jsonComplaint.getString("station"),
                                        jsonComplaint.getString("seat-no"),
                                        jsonComplaint.getString("department"),
                                        jsonComplaint.getBoolean("new"),
                                        jsonComplaint.getString("email"),
                                        "HH:MM"
                                );
//                                */
                            listItems.add(item);
                                Log.d(TAG, "onResponse: in response for loop");
                            }
                            Log.d(TAG, "onResponse: dismissing progressdialog");
                            progressDialog.dismiss();
                            Log.d(TAG, "onResponse: progressdialog dismissed");
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                progressDialog.dismiss();
                Log.d(TAG, "onErrorResponse: volley error");
            }

        });

        RequestQueue requestQueue = Volley.newRequestQueue(this);
        Log.d(TAG, "loadRecyclerViewData: requestQueue");
        requestQueue.add(stringRequest);
        Log.d(TAG, "loadRecyclerViewData: after returnQueue");
    }


    public static class SimpleItemRecyclerViewAdapter
            extends RecyclerView.Adapter<SimpleItemRecyclerViewAdapter.ViewHolder> {

        //        private final ItemListActivity mParentActivity;
//        private final List<DummyContent.DummyItem> mValues;
        private final boolean mTwoPane;
        private Context context;
        private final ItemListActivity mParentActivity;
        private List<MyDataset> listItems;
        private int pos;

        public SimpleItemRecyclerViewAdapter(ItemListActivity parent, boolean mTwoPane, Context context, List<MyDataset> listItems) {
            this.mTwoPane = mTwoPane;
            this.context = context;
            this.listItems = listItems;
            mParentActivity = parent;
        }


        private final View.OnClickListener mOnClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//                DummyContent.DummyItem item = (DummyContent.DummyItem) view.getTag();
//                MyDataset item = (MyDataset) view.getTag();

//                Log.d(TAG, "onClick: MyDataset"+item.toString());


//                Log.d(TAG, "onClick: View Clicked");
//                if (mTwoPane) {
//                    Bundle arguments = new Bundle();
//                    arguments.putString(ItemDetailFragment.ARG_ITEM_ID, item.id);
//                    ItemDetailFragment fragment = new ItemDetailFragment();
//                    fragment.setArguments(arguments);
//                    mParentActivity.getSupportFragmentManager().beginTransaction()
//                            .replace(R.id.item_detail_container, fragment)
//                            .commit();
//                } else {
//                Context context = view.getContext();
//                Context context = view.getContext();
//                Intent intent = new Intent(context, ItemDetailActivity.class);
//
//                try{
//                    intent.putExtra("complatintId", item.getComplaintIdString());
//                    intent.putExtra("complaint", item.getComplaint());
//                    intent.putExtra("time", item.getTime());
//                }catch (Exception e) {
//                    Log.e(TAG, "onClick: " + e.getMessage());
//                }

                //MyDataset item = (MyDataset) view.getTag();
                int pos = (int) view.getTag();
                if (mTwoPane) {
                    Bundle arguments = new Bundle();
//                    arguments.putString(ItemDetailFragment.ARG_ITEM_ID, item.getComplaintIdString());
                    ItemDetailFragment fragment = new ItemDetailFragment();
                    fragment.setArguments(arguments);
                    mParentActivity.getSupportFragmentManager().beginTransaction()
                            .replace(R.id.item_detail_container, fragment)
                            .commit();
                } else {
                    Context context = view.getContext();

                    MyDataset item = listItems.get(pos);

                    Log.d(TAG, "onClick: MyDataset "+item.getComplaintIdString()+item.getQuery()+item.getStation());

                    Intent intent = new Intent(context, ItemDetailActivity.class);
//                    intent.putExtra(ItemDetailFragment.ARG_ITEM_ID, item.getComplaintIdString());
                    intent.putExtra("MyDataset", item);


                    mParentActivity.startActivityForResult(intent, 1);

                }

//                Log.d(TAG, "onClick: Extra added");
//                context.startActivity(intent);
//                }
            }
        };


        class ViewHolder extends RecyclerView.ViewHolder {
            //            final TextView mIdView;
            private TextView textViewComplaint;
            private TextView textViewComplaintId;
            private TextView textViewTime;


            ViewHolder(View view) {
                super(view);
//                mIdView = (TextView) view.findViewById(R.id.id_text);
                textViewComplaint = view.findViewById(R.id.complaint);
                textViewComplaintId = view.findViewById(R.id.complaint_id);
                textViewTime = view.findViewById(R.id.complaint_time);

            }
        }

        @Override
        public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
            View view = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.complaint_view_small, parent, false);
            view.setOnClickListener(mOnClickListener);
            return new ViewHolder(view);
        }

        @Override
        public void onBindViewHolder(final ViewHolder holder, int position) {
//            holder.mIdView.setText(mValues.get(position).id);
//            holder.mContentView.setText(mValues.get(position).content);
//            holder.itemView.setTag(mValues.get(position));
//            holder.itemView.setOnClickListener(mOnClickListener);
            MyDataset listItem = listItems.get(position);

//            Log.d(TAG, "onBindViewHolder: string" + listItem.toString());

            if(listItem.getNewComplaint()==false)
                holder.itemView.setBackgroundColor((int)R.color.gray);

            holder.itemView.setTag(position);
            holder.textViewComplaint.setText(listItem.getQuery());
            holder.textViewTime.setText(listItem.getTime());
            holder.textViewComplaintId.setText(listItem.getComplaintIdString());
        }

        @Override
        public int getItemCount() {
            return listItems.size();
        }
    }

}
