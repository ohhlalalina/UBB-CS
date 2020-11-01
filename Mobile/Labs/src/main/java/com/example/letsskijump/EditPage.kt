package com.example.letsskijump
import android.content.Context
import android.content.Intent
import android.os.Bundle
import com.google.android.material.floatingactionbutton.FloatingActionButton
import android.util.Log
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import com.example.letsskijump.ChangeEvent
import com.example.letsskijump.Controller.Controller
import com.example.letsskijump.Model.Event
import com.example.letsskijump.R
import kotlinx.android.synthetic.main.activity_edit_page.*


class EditPage : AppCompatActivity() {

    private var listEvents = ArrayList<Event>()
    var c = Controller()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_edit_page)

        val floatingActionButton = findViewById<FloatingActionButton>(R.id.add_events)
        floatingActionButton.setOnClickListener {
            var intent = Intent(this, ChangeEvent::class.java)
            startActivity(intent)
        }

        loadQueryAll()

        list_events.onItemClickListener = AdapterView.OnItemClickListener { adapterView, view, position, id ->
            Toast.makeText(this, "Click on " + listEvents[position].name, Toast.LENGTH_SHORT).show()
        }
    }

    override fun onResume() {
        super.onResume()
        loadQueryAll()
    }

    fun loadQueryAll() {

        //var dbManager = NoteDbManager(this)
        //var c = Controller()
        val ev = c.getEvents()
        //val cursor = dbManager.queryAll()

        listEvents.clear()

        if (ev != null) {
            for (event in ev){
                listEvents.add(event)
            }
        }

        var eventsAdapter = EventsAdapter(this, listEvents)
        list_events.adapter = eventsAdapter
    }

    inner class EventsAdapter : BaseAdapter {

        private var eventsList = ArrayList<Event>()
        private var context: Context? = null

        constructor(context: Context, eventsList: ArrayList<Event>) : super() {
            this.eventsList = eventsList
            this.context = context
        }

        override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View? {

            val view: View?
            val vh: ViewHolder

            if (convertView == null) {
                view = layoutInflater.inflate(R.layout.event, parent, false)
                vh = ViewHolder(view)
                view.tag = vh
                Log.i("JSA", "set Tag for ViewHolder, position: " + position)
            } else {
                view = convertView
                vh = view.tag as ViewHolder
            }

            var mEvent = eventsList[position]

            vh.eventTitle.text = mEvent.getTitle()
            vh.eventDescription.text = mEvent.getDesc()

            vh.buttonEdit.setOnClickListener {
                updateEvent(mEvent)
            }

            vh.buttonDelete.setOnClickListener {
                //var c = Controller()
                val selectionArgs = mEvent.id
                c.removeEvent(selectionArgs)
                loadQueryAll()
            }

            return view
        }

        override fun getItem(position: Int): Any {
            return eventsList[position]
        }

        override fun getItemId(position: Int): Long {
            return position.toLong()
        }

        override fun getCount(): Int {
            return eventsList.size
        }
    }

    private fun updateEvent(event: Event) {
        var intent = Intent(this, ChangeEvent::class.java)
        intent.putExtra("MainActName", event.name)
        intent.putExtra("MainActDescription", event.description)
        intent.putExtra("MainActHill", event.hill)
        intent.putExtra("MainActLocation", event.location)
        intent.putExtra("MainActStartDate", event.startDate)
        intent.putExtra("MainActStartHour", event.startHour)
        startActivity(intent)
    }

    private class ViewHolder(view: View?) {
        val eventTitle: TextView
        val eventDescription: TextView
        val buttonEdit: ImageView
        val buttonDelete: ImageView

        init {
            this.eventTitle = view?.findViewById(R.id.eventTitle) as TextView
            this.eventDescription = view?.findViewById(R.id.eventDescription) as TextView
            this.buttonEdit = view?.findViewById(R.id.buttonEdit) as ImageView
            this.buttonDelete = view?.findViewById(R.id.buttonDelete) as ImageView
        }
    }

}
