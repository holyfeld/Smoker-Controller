Smoker Controller

update 2024-07-13

“If you wait by the river long enough, the bodies of your enemies will float by.”
― Sun Tzu 

paraphrasing for this project ...

If you wait long enough, someone will solve the problem better than you might have. - Old Cranky Guy

tl;dr

Started looking around and found https://nebhead.github.io/PiFire/ 
Got to be honest. This project has more stuff in it than I might have done.
And it's got great documentaton and an active user base. 

I still want to improve my smoker control and data gathering. The Traeger controller is more complex than what the MES40 needs.

Does it make sense to update this project? Possibly. I'll need a different control output device. And as we used to say in the '80s.
If you have data in two places in the database, it's wrong in at least one of them.

More as I move along.

Rev 0.5 220116-12-11 list the parts explain the thinking

Background - Rev 0.5

Rev 0.5

I want to update the control system on my Masterbuilt MES-40. This smoker currently uses an Auber PID controller with a
thermistor probe in the smoker chamber. The 10A heating element plugs into the back of the Auber. The Auber uses a TPO
to control the on/off cycles which controls the chamber temp. Temperature set point is set via the front panel on the
Auber.

I've used various iGrill software for seeing/logging chamber and meat internal temperature. Data logging (for trends)
can be exported as a cvs file, and a PDF graph. Over time the # of temperature sensors increased (up to 4) with a
corresponding degradation of viewing trending. In fairness, I've not tried the new software on my iPad, only my iPhone.

Moving forward, the basic parts:

Raspberry PI, latest and greatest model
The ability to read 4 thermocouples. One will be for chamber temperature
(http://www.auberins.com/index.php?main_page=product_info&cPath=20_3&products_id=101),
the other three will be used for one or more meat internal temperatures.
http://www.auberins.com/index.php?main_page=product_info&cPath=20_3&products_id=56
Currently thinking a USB interface for this.
http://www.robotshop.com/en/phidgettemperaturesensor-4-input-usb-thermocouple-interface.html
SSR for sending power to the chamber heating element (120VAC/1200W).
http://www.robotshop.com/en/40a-ssr-relay.html or
http://www.auberins.com/index.php?main_page=product_info&products_id=393
Or maybe a 0 - 5 output to fire the Auber SSR so I don’t have to mess with the TPO calculations.
(Future) a local touch screen interface similar to https://www.adafruit.com/products/2395
Some interface plate to allow access to the GPIO for firing the SSR (#3) and interfacing to the (future) touch screen.
Power supply
Terminal strip(s).
An enclosure for mounting the above stuff.

And the functions:

Set and view the desired smoker chamber temperature.
Control to the set temperature. Initially we will focus only on steady state temperatures, no ramp/soak.
View controller output (0 - 100%).
View controller tuning parameters.
Set controller tuning parameters.
View controller Auto / Manual state.
Set controller Auto / Manual state.
View (up to 4) temperature inputs.
Assign names to each of the 4 thermocouple inputs for logging and trending purposes,
Allow a name to be entered for storing the trend data.
Displaying the trend data.
View alarms?
Set alarms?
Emergency conditions?
Clean exit (shut down all outputs). Which begs a question, can this be set up fail safe, or is that implicit as when
the RPi loses power, the SSR will (should?) lose power also.



ToDos: research PID loops with TPO.


