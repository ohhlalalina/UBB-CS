package com.example.letsskijump.Controller
import com.example.letsskijump.Model.Event
import android.os.Build
import androidx.annotation.RequiresApi
import kotlin.math.log

class Controller {
    private
    companion object{
        var events: MutableList<Event> = mutableListOf()
    }

    constructor() {
            events.add(
                Event(
                    1, "WC Event Qualifications", "Men",
                    "Wisla Malinka Hill - 134 m.", "Wisla, Polska", "20.11.2020","18:00 CET"
                )
            )
            events.add(
                Event(
                    2, "WC Event Teams", "Men",
                    "Wisla Malinka Hill - 134 m.", "Wisla, Polska", "21.11.2020","16:00 CET"
                )
            )
            events.add(
            Event(
                3, "WC Event Individual", "Men",
                "Wisla Malinka Hill - 134 m.", "Wisla, Polska", "22.11.2020","16:00 CET"
            ))
            events.add(
                Event(
                    4, "WC Event Qualifications", "Men",
                    "Rukatunturi Hill - 142 m.", "Ruka, Finland", "27.11.2020","16:45 CET"
                ))
            events.add(
                Event(
                    5, "WC Event Individual", "Men",
                    "Rukatunturi Hill - 142 m.", "Ruka, Finland", "28.11.2020","16:30 CET"
                ))
            events.add(
                Event(
                    6, "WC Event Individual", "Men",
                    "Rukatunturi Hill - 142 m.", "Ruka, Finland", "29.11.2020","15:30 CET"
                ))

        }

    fun maxId(): Int{
        var id : Int = 0;
        for(event in events)
            if(event.id > id)
                id = event.id
        return id
    }

    fun addEvent(event: Event){
        val id : Int = maxId() + 1
        event.id = id;
        events.add(event)
    }


    fun removeEvent(id: Int): Boolean{
        var pos = -1;
        for(i in 0..events.size-1)
            if(events[i].id == id)
                pos = i;
        if(pos>-1) {
            events.removeAt(pos)
            return true
        }
        return false
    }


    fun updateEvent(e: Event): Int {
        for(event in events){
            if(event.id == e.id){
                event.name = e.name
                event.description = e.description
                event.hill = e.hill
                event.location = e.location
                event.startDate = e.startDate
                event.startHour = e.startHour
                return 1
            }
        }
        return 0
    }

    fun getEvent(id: Int): Event?{
        for(event in events)
            if(event.id == id)
                return event
        return null
    }

    fun getEvents(): MutableList<Event>?{
        return events
    }
}