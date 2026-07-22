# Ai-AQI

Smart IoT-based air quality monitoring system with real-time data tracking and AI prediction <br>
it would basically contains two sides first is the hardware and second will be the software which is the main part in it.

## Current Progress

Repository structure completed <br>
Hardware connection planning completed <br>
Basic ESP32 sensor reading code added <br>
Preparing for live hardware testing <br>
Dataset uploaded for AQI prediction model <br>
Dataset preprocessing completed <br>
Initial AQI prediction model training started <br>
Currently using PM2.5 as the initial parameter for prediction <br>
Basic frontend dashboard created using HTML and CSS <br>
AQI monitoring cards added to dashboard <br>
Predicted AQI section added <br>
AQI graph placeholder added for future visualization <br>
System architecture documented <br>

### System Architecture

The following diagram represents the workflow of the AI-driven air quality monitoring and prediction system.

![Workflow](architecture/workflow_related/ai-workflow-diagram.png)

## Future Work

Complete AQI prediction model training using multiple parameters <br>
Backend development and API integration <br>
Frontend and backend connection <br>
Cloud database integration <br>
ESP32 live data collection and testing <br>
Alert system implementation <br>
Final deployment and project demonstration <br>

## Resumed project development work  again 
Resumed project development after a short break and continuing with model improvement and backend integration. <br>
## Future Improvements

- Real-time sensor integration with ESP32.
- Live AQI dashboard.
- Historical AQI visualization.
- Deployment on cloud.
### Run the backend

```bash
python app.py
```

### Upload ESP32 Code

Update the Wi-Fi credentials and Flask server IP in the ESP32 code before uploading it to the board.

## Author

**Priyanshu Sharma**

B.Tech IoT Student

Frontend improvements.
Connect frontend to the prediction API (if not already).
Improve the UI with AQI cards and status.
Add screenshots/GIFs of the working project.
Final cleanup (requirements.txt, .gitignore, deployment notes).

At that point, your repository will have a coherent, realistic development history instead of looking like everything was uploaded in one go.
