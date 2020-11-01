package com.example.letsskijump

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.WindowManager
import androidx.appcompat.app.AlertDialog
import kotlinx.android.synthetic.main.activity_login.*

class Login : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        login_button.setOnClickListener {
            try {
                val username = usernameField.editText?.text.toString()
                val password = passwordField.editText?.text.toString()
                if(username == null || password == null){
                    throw Exception("Username or Password can't be empty!")
                }
                if(username == "admin" && password == "admin") {
                    val intent = Intent(this, EditPage::class.java)
                    intent.putExtra("USERNAME", username);
                    startActivity(intent);
                }
                else if(username == "user"){
                    val intent = Intent(this, ShowPage::class.java)
                    intent.putExtra("USERNAME", username);
                    startActivity(intent);
                }
                else {
                    AlertDialog.Builder(this)
                        .setTitle("Log-in failed")
                        .setPositiveButton("Ok", null)
                        .show()
                }
            }
            catch (e: Exception) {
                AlertDialog.Builder(this).setTitle(e.message).setPositiveButton("Ok", null).show()
            }
        }
    }

}