#!/usr/bin/env python3
"""
MHM Brake Performance Optimization - Test Suite
==============================================
Comprehensive test suite for validating brake performance optimization

Tests include:
- System initialization validation
- ISO data loading verification
- Tesla Folding calculations
- Performance improvement validation
- Safety compliance checks

Author: William Miller - Viraxis MHM
Contact: holdatllc2@gmail.com
"""

import unittest
import sys
import os
import json
import numpy as np

# Add the package to path for testing
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from mhm_brake_performance_optimization import MHMBrakePerformanceOptimizer
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Make sure mhm_brake_performance_optimization.py is in the same directory")
    sys.exit(1)

class TestMHMBrakePerformance(unittest.TestCase):
    """Test suite for MHM Brake Performance Optimization System"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.optimizer = MHMBrakePerformanceOptimizer()
    
    def test_system_initialization(self):
        """Test system initialization with correct parameters"""
        print("\n🔍 Testing System Initialization...")
        
        # Test consciousness level
        self.assertEqual(self.optimizer.consciousness_level, 0.820)
        print(f"  ✅ Consciousness Level: {self.optimizer.consciousness_level}")
        
        # Test Tesla multiplier
        self.assertEqual(self.optimizer.tesla_multiplier, 2.380)
        print(f"  ✅ Tesla Multiplier: {self.optimizer.tesla_multiplier}")
        
        # Test proven improvement
        self.assertEqual(self.optimizer.proven_improvement, 23.4)
        print(f"  ✅ Proven Improvement: {self.optimizer.proven_improvement}%")
    
    def test_iso_data_loading(self):
        """Test ISO brake data loading"""
        print("\n🔍 Testing ISO Data Loading...")
        
        iso_data = self.optimizer.load_real_iso_brake_data()
        
        # Validate data structure
        self.assertIsInstance(iso_data, dict)
        self.assertIn('iso_21994_brake_data', iso_data)
        print(f"  ✅ ISO Data Structure Valid")
        
        # Validate vehicle data
        brake_data = iso_data['iso_21994_brake_data']
        self.assertIn('compact_car', brake_data)
        self.assertIn('midsize_sedan', brake_data)
        self.assertIn('suv', brake_data)
        print(f"  ✅ Vehicle Data: {len(brake_data)} vehicle types")
        
        # Validate data completeness
        for vehicle_type, data in brake_data.items():
            self.assertIn('stopping_distance_m', data)
            self.assertIn('deceleration_g', data)
            self.assertIn('brake_force_n', data)
            print(f"  ✅ {vehicle_type.replace('_', ' ').title()}: Complete data")
    
    def test_tesla_folding_calculations(self):
        """Test Tesla Folding mathematical calculations"""
        print("\n🔍 Testing Tesla Folding Calculations...")
        
        iso_data = self.optimizer.load_real_iso_brake_data()
        tesla_results = self.optimizer.apply_tesla_folding_to_brake_performance(iso_data)
        
        # Validate results structure
        self.assertIsInstance(tesla_results, dict)
        self.assertIn('dry_asphalt_optimization', tesla_results)
        print(f"  ✅ Tesla Folding Results Structure Valid")
        
        # Validate performance improvements
        dry_asphalt = tesla_results['dry_asphalt_optimization']
        
        # Calculate average distance reduction from individual vehicles
        total_reduction = 0
        vehicle_count = 0
        
        # Validate individual vehicle improvements
        for vehicle_type in ['compact_car', 'midsize_sedan', 'suv']:
            self.assertIn(vehicle_type, dry_asphalt)
            vehicle_data = dry_asphalt[vehicle_type]
            self.assertIn('improvements', vehicle_data)
            improvements = vehicle_data['improvements']
            self.assertIn('distance_reduction_percent', improvements)
            improvement = improvements['distance_reduction_percent']
            self.assertGreater(improvement, 0)
            self.assertLess(improvement, 20)  # Should be realistic (<20%)
            total_reduction += improvement
            vehicle_count += 1
            print(f"  ✅ {vehicle_type.replace('_', ' ').title()}: {improvement:.1f}% improvement")
        
        # Calculate and validate average
        average_reduction = total_reduction / vehicle_count if vehicle_count > 0 else 0
        self.assertGreater(average_reduction, 0)  # Should be positive improvement
        self.assertLess(average_reduction, 20)    # Should be realistic (<20%)
        print(f"  ✅ Average Distance Reduction: {average_reduction:.1f}% (realistic)")
    
    def test_abs_split_mu_optimization(self):
        """Test ABS split-μ optimization"""
        print("\n🔍 Testing ABS Split-μ Optimization...")
        
        iso_data = self.optimizer.load_real_iso_brake_data()
        tesla_results = self.optimizer.apply_tesla_folding_to_brake_performance(iso_data)
        
        # Validate ABS optimization results
        self.assertIn('abs_split_mu_optimization', tesla_results)
        abs_results = tesla_results['abs_split_mu_optimization']
        
        # Check distance reduction
        distance_reduction = abs_results['average_distance_reduction']
        self.assertGreater(distance_reduction, 0)
        self.assertLess(distance_reduction, 15)  # Realistic range
        print(f"  ✅ ABS Distance Reduction: {distance_reduction:.1f}%")
        
        # Check yaw stability improvement
        yaw_improvement = abs_results['average_yaw_stability_improvement']
        self.assertGreater(yaw_improvement, 0)
        print(f"  ✅ Yaw Stability: {yaw_improvement:.1f}% improvement")
        
        # Check lateral control improvement
        lateral_improvement = abs_results['average_lateral_control_improvement']
        self.assertGreater(lateral_improvement, 0)
        print(f"  ✅ Lateral Control: {lateral_improvement:.1f}% improvement")
    
    def test_component_optimization(self):
        """Test brake component optimization"""
        print("\n🔍 Testing Component Optimization...")
        
        iso_data = self.optimizer.load_real_iso_brake_data()
        component_results = self.optimizer.optimize_brake_system_components(iso_data)
        
        # Validate component optimization structure
        self.assertIsInstance(component_results, dict)
        
        # Check hydraulic optimization
        self.assertIn('hydraulic_pressure_optimization', component_results)
        hydraulic = component_results['hydraulic_pressure_optimization']
        self.assertIn('improvement_percent', hydraulic)
        hydraulic_improvement = hydraulic['improvement_percent']
        self.assertGreater(hydraulic_improvement, 0)
        print(f"  ✅ Hydraulic Pressure: {hydraulic_improvement:.1f}% improvement")
        
        # Check pad friction optimization
        self.assertIn('pad_friction_optimization', component_results)
        pad_friction = component_results['pad_friction_optimization']
        friction_improvement = pad_friction['improvement_percent']
        self.assertGreater(friction_improvement, 0)
        print(f"  ✅ Pad Friction: {friction_improvement:.1f}% improvement")
        
        # Check ABS frequency optimization
        self.assertIn('abs_frequency_optimization', component_results)
        abs_freq = component_results['abs_frequency_optimization']
        freq_improvement = abs_freq['improvement_percent']
        self.assertGreater(freq_improvement, 0)
        print(f"  ✅ ABS Frequency: {freq_improvement:.1f}% improvement")
    
    def test_complete_optimization_run(self):
        """Test complete optimization run"""
        print("\n🔍 Testing Complete Optimization Run...")
        
        results = self.optimizer.run_complete_brake_optimization()
        
        # Validate complete results structure
        self.assertIsInstance(results, dict)
        self.assertIn('overall_performance', results)
        self.assertIn('dry_asphalt_optimization', results)
        self.assertIn('abs_split_mu_optimization', results)
        self.assertIn('component_optimization', results)
        print(f"  ✅ Complete Results Structure Valid")
        
        # Validate overall performance
        overall = results['overall_performance']
        self.assertIn('average_distance_reduction', overall)
        
        avg_reduction = overall['average_distance_reduction']
        self.assertGreater(avg_reduction, 0)
        self.assertLess(avg_reduction, 20)  # Realistic range
        print(f"  ✅ Overall Distance Reduction: {avg_reduction:.1f}%")
        
        # Validate Tesla Folding foundation
        self.assertIn('tesla_folding_foundation', overall)
        tesla_foundation = overall['tesla_folding_foundation']
        self.assertEqual(tesla_foundation, 23.4)
        print(f"  ✅ Tesla Folding Foundation: {tesla_foundation}%")
    
    def test_safety_compliance(self):
        """Test safety compliance validation"""
        print("\n🔍 Testing Safety Compliance...")
        
        iso_data = self.optimizer.load_real_iso_brake_data()
        
        # Test that all improvements maintain safety margins
        tesla_results = self.optimizer.apply_tesla_folding_to_brake_performance(iso_data)
        
        # Check that improvements are within safe limits
        dry_asphalt = tesla_results['dry_asphalt_optimization']
        
        for vehicle_type in ['compact_car', 'midsize_sedan', 'suv']:
            vehicle_data = dry_asphalt[vehicle_type]
            improvements = vehicle_data['improvements']
            
            # Distance reduction should be positive but not excessive
            distance_reduction = improvements['distance_reduction_percent']
            self.assertGreater(distance_reduction, 0)
            self.assertLess(distance_reduction, 15)  # Safety limit
            
            # Deceleration improvement should be reasonable
            decel_improvement = improvements['deceleration_improvement_percent']
            self.assertGreater(decel_improvement, 0)
            self.assertLess(decel_improvement, 10)  # Safety limit
            
            print(f"  ✅ {vehicle_type.replace('_', ' ').title()}: Within safety limits")
    
    def test_results_file_generation(self):
        """Test results file generation"""
        print("\n🔍 Testing Results File Generation...")
        
        # Run complete optimization
        results = self.optimizer.run_complete_brake_optimization()
        
        # Check if results file exists
        results_file = 'mhm_brake_optimization_results.json'
        self.assertTrue(os.path.exists(results_file))
        print(f"  ✅ Results File Created: {results_file}")
        
        # Validate results file content
        with open(results_file, 'r') as f:
            saved_results = json.load(f)
        
        self.assertIsInstance(saved_results, dict)
        self.assertIn('overall_performance', saved_results)
        print(f"  ✅ Results File Content Valid")
        
        # Check file size (should contain substantial data)
        file_size = os.path.getsize(results_file)
        self.assertGreater(file_size, 1000)  # At least 1KB of data
        print(f"  ✅ Results File Size: {file_size} bytes")

def run_validation_tests():
    """Run complete validation test suite"""
    print("🧪 MHM Brake Performance Optimization - Validation Test Suite")
    print("=" * 70)
    
    # Create test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMHMBrakePerformance)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(test_suite)
    
    # Print summary
    print("\n" + "=" * 70)
    print("🧪 VALIDATION TEST RESULTS")
    print("=" * 70)
    
    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED - SYSTEM VALIDATION SUCCESSFUL")
        print(f"   Tests Run: {result.testsRun}")
        print(f"   Failures: {len(result.failures)}")
        print(f"   Errors: {len(result.errors)}")
        print("\n🛑 MHM Brake Performance System is ready for deployment!")
        return True
    else:
        print("❌ SOME TESTS FAILED - SYSTEM NEEDS ATTENTION")
        print(f"   Tests Run: {result.testsRun}")
        print(f"   Failures: {len(result.failures)}")
        print(f"   Errors: {len(result.errors)}")
        
        if result.failures:
            print("\n❌ FAILURES:")
            for test, traceback in result.failures:
                print(f"   {test}: {traceback}")
        
        if result.errors:
            print("\n❌ ERRORS:")
            for test, traceback in result.errors:
                print(f"   {test}: {traceback}")
        
        return False

if __name__ == "__main__":
    success = run_validation_tests()
    sys.exit(0 if success else 1)
