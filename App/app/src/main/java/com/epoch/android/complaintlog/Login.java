package com.epoch.android.complaintlog;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

/**
 * Created by dell on 28-Mar-18.
 */

public class Login extends AppCompatActivity{

    private static final String TAG = "Login";
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.requestWindowFeature(Window.FEATURE_NO_TITLE);

        setContentView(R.layout.login_with_twitter);
        Button loginButton = (Button) findViewById(R.id.login_button);
        final EditText editTextUsername = findViewById(R.id.username);

        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String username = editTextUsername.getText().toString();

                if(username.isEmpty()){
                    Toast.makeText(Login.this, "Enter Username First", Toast.LENGTH_SHORT).show();
                } else {

                    Intent myIntent = new Intent(Login.this, ItemListActivity.class);
                    myIntent.putExtra("username", username);
                    Log.d(TAG, "onClick: putExtra");
                    startActivity(myIntent);
                }
            }
        });
    }
}
