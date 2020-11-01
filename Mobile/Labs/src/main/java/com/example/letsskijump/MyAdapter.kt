package com.example.letsskijump

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AbsListView
import android.widget.ArrayAdapter
import android.widget.TextView
import com.example.letsskijump.Model.Event
import java.text.FieldPosition

class MyAdapter(var mCtx: Context, var resources: Int, var items:List<Event>):ArrayAdapter<Event>(mCtx, resources,items) {
    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View{
        val layoutInflater:LayoutInflater = LayoutInflater.from(mCtx)
        val view:View = layoutInflater.inflate(resources, null)

        val titleTextView:TextView = view.findViewById(R.id.textView1)
        val descriptionTextView: TextView = view.findViewById(R.id.textView2)

        var mItem:Event = items[position]
        titleTextView.text = mItem.getTitle()
        descriptionTextView.text = mItem.getDesc()

        return view
    }
}