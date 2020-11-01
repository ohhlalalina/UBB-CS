package com.example.letsskijump

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.letsskijump.Controller.Controller
import com.example.letsskijump.Model.Event

import kotlinx.android.synthetic.main.activity_change_event.*

class ChangeEvent : AppCompatActivity() {
    var id = 0
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_change_event)
        try {
            var bundle: Bundle = intent.extras
            id = bundle.getInt("MainActId", 0)
            if (id != 0) {
                edtName.setText(bundle.getString("MainActName"))
                edtDescription.setText(bundle.getString("MainActDescription"))
                edtLocation.setText(bundle.getString("MainActLocation"))
                edtHill.setText(bundle.getString("MainActHill"))
                edtStartDate.setText(bundle.getString("MainActStartDate"))
                edtStartHour.setText(bundle.getString("MainActStartHour"))
            }
        } catch (ex: Exception) {
        }

        btAdd.setOnClickListener {
            //var dbManager = NoteDbManager(this)
            var c = Controller()

            var e = Event(0,edtName.text.toString(),edtDescription.text.toString(),edtHill.text.toString(),edtLocation.text.toString(),edtStartDate.text.toString(),edtStartHour.text.toString())

            if (id == 0) {
                c.addEvent(e)
                var mID = e.getID()

                if (mID != null) {
                    if (mID > 0) {
                        Toast.makeText(this, "Add event successfully!", Toast.LENGTH_LONG).show()
                        finish()
                    } else {
                        Toast.makeText(this, "Fail to add event!", Toast.LENGTH_LONG).show()
                    }
                }
            } else {
                var selectionArs = arrayOf(id.toString())
                val mID = c.updateEvent(e)

                if (mID > 0) {
                    Toast.makeText(this, "Modified event successfully!", Toast.LENGTH_LONG).show()
                    finish()
                } else {
                    Toast.makeText(this, "Failed to modify event!", Toast.LENGTH_LONG).show()
                }
            }
        }
    }
}

