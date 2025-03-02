import 'dart:io';
import 'package:flutter/material.dart';
import 'package:path/path.dart' as p;
import 'dart:async';
import 'dart:convert';
//import 'package:flutter_tts/flutter_tts.dart';

void main() {
  runApp(SurveyApp());
}

class SurveyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: SurveyScreen(),
    );
  }
}

class SurveyScreen extends StatefulWidget {
  @override
  _SurveyScreenState createState() => _SurveyScreenState();
}

class _SurveyScreenState extends State<SurveyScreen> {
  final List<String> symptoms = [
    'Headache',
    'Fever',
    'Cough',
    'Fatigue',
    'Sore Throat',
  ];

  final Map<String, bool> symptomResponses = {}; // Store responses

  @override
  void initState() {
    super.initState();
    for (var symptom in symptoms) {
      symptomResponses[symptom] = false; // Initialize all to false
    }
  }

  void _runPythonScript(String scriptName, BuildContext context) async {
    try {
      final process = await Process.run('python',
        [ 
          p.join('healthbulb_main', 'lib', scriptName),
        ],
      ); // Ensure script is in assets
      if (process.exitCode == 0) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('$scriptName executed successfully!')),
        );
        print('Script output: ${process.stdout}');
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Error running $scriptName: ${process.stderr}')),
        );
        print('Script error: ${process.stderr}');
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('An error occurred: $e')),
      );
      print('Error: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Symptom Survey')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            Text('Select your symptoms:', style: TextStyle(fontSize: 18)),
            SizedBox(height: 16),
            Wrap(
              spacing: 8.0,
              runSpacing: 4.0,
              children: symptoms.map((symptom) {
                return ElevatedButton(
                  onPressed: () {
                    setState(() {
                      symptomResponses[symptom] = !symptomResponses[symptom]!;
                    });
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: symptomResponses[symptom]! ? Colors.black : null,
                  ),
                  child: Text(symptom),
                );
              }).toList(),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                _runPythonScript('tts_reccomendations.py', context); // Example Python script
              },
              child: Text('Run Symptom Analysis'), //link to tts_reccomendations.py
            ),
            ElevatedButton(
              onPressed: () {
                _runPythonScript('pdf_to_text.py', context); // Example other Python Script
              },
              child: Text('Use Text-to-Speech'),
            )
          ],
        ),
      ),
    );
  }
}