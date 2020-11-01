package com.example.letsskijump

import android.content.Context
import android.os.Bundle
//import android.support.v7.app.AppCompatActivity
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import android.widget.AdapterView.OnItemClickListener
import androidx.annotation.Nullable
import androidx.appcompat.app.AppCompatActivity
//import androidx.test.core.app.ApplicationProvider.getApplicationContext
import com.example.letsskijump.Controller.Controller
import com.example.letsskijump.Model.Event


class ShowPage : AppCompatActivity() {
    private val c: Controller = Controller()
    private lateinit var events: MutableList<Event>;
    private lateinit var adapter: MyAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_show_page)

        var listview = findViewById<ListView>(R.id.listView)
        var list = mutableListOf<Event>()
        events = c.getEvents()!!
        for(event in events) {
            list.add(event)
        }
        listview.adapter = MyAdapter(this,R.layout.row,list)

    }
}


