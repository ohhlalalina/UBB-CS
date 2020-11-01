package com.example.letsskijump.Model
import com.example.letsskijump.Controller.Controller
import java.io.Serializable;

class Event (
        var id: Int,
        var name: String,
        var description: String,
        var hill: String,
        var location: String,
        var startDate: String,
        var startHour: String): Serializable{

        fun getTitle(): String?{
                return name
        }

        fun getDesc(): String?{
                return "$description $hill $location $startDate $startHour"
        }

        fun getID(): Int?{
                return id
        }
}