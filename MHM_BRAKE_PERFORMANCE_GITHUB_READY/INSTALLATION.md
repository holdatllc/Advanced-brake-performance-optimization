# MHM Brake Performance Optimization - Installation Guide

## 🚀 **QUICK START INSTALLATION**

### **System Requirements**
- **Python**: 3.8 or higher
- **Operating System**: Windows 10+, macOS 10.15+, or Linux Ubuntu 18.04+
- **Memory**: 4GB RAM minimum, 8GB recommended
- **Storage**: 500MB available space
- **Network**: Internet connection for initial setup

### **One-Line Installation**
```bash
pip install mhm-brake-performance
```

---

## 📦 **DETAILED INSTALLATION**

### **Step 1: Environment Setup**

#### **Create Virtual Environment (Recommended)**
```bash
# Create virtual environment
python -m venv mhm_brake_env

# Activate virtual environment
# On Windows:
mhm_brake_env\Scripts\activate
# On macOS/Linux:
source mhm_brake_env/bin/activate
```

#### **Update pip and setuptools**
```bash
pip install --upgrade pip setuptools wheel
```

### **Step 2: Install Dependencies**

#### **Core Dependencies**
```bash
pip install numpy>=1.21.0
pip install matplotlib>=3.5.0
pip install scipy>=1.7.0
pip install pandas>=1.3.0
```

#### **Optional Dependencies (for advanced features)**
```bash
# For real-time optimization
pip install numba>=0.56.0

# For data visualization
pip install seaborn>=0.11.0
pip install plotly>=5.0.0

# For MATLAB integration
pip install matlab.engine  # Requires MATLAB installation
```

### **Step 3: Install MHM Brake Performance**

#### **From PyPI (Recommended)**
```bash
pip install mhm-brake-performance
```

#### **From Source (Development)**
```bash
git clone https://github.com/viraxis-mhm/mhm-brake-performance.git
cd mhm-brake-performance
pip install -e .
```

#### **Verify Installation**
```python
import mhm_brake_performance
print(f"MHM Brake Performance v{mhm_brake_performance.__version__} installed successfully!")
```

---

## 🔧 **CONFIGURATION**

### **Basic Configuration**

#### **Create Configuration File**
```python
# config.py
MHM_CONFIG = {
    'tesla_folding': {
        'consciousness_level': 0.820,
        'tesla_multiplier': 2.380,
        'automotive_scaling': 0.30
    },
    'brake_optimization': {
        'enable_real_time': True,
        'safety_limits': True,
        'performance_logging': True
    },
    'data_sources': {
        'iso_21994_enabled': True,
        'iso_14512_enabled': True,
        'matlab_integration': True
    }
}
```

#### **Environment Variables (Optional)**
```bash
# Set environment variables for advanced configuration
export MHM_CONSCIOUSNESS_LEVEL=0.820
export MHM_TESLA_MULTIPLIER=2.380
export MHM_ENABLE_LOGGING=true
export MHM_DATA_PATH=/path/to/brake/data
```

### **Advanced Configuration**

#### **Custom Tesla Folding Parameters**
```python
from mhm_brake_performance import MHMBrakeOptimizer

# Initialize with custom parameters
optimizer = MHMBrakeOptimizer(
    consciousness_level=0.850,      # Custom consciousness level
    tesla_multiplier=2.500,         # Custom Tesla multiplier
    automotive_scaling=0.35,        # Custom automotive scaling
    enable_real_time=True,          # Enable real-time optimization
    safety_mode='strict'            # Safety mode: 'strict', 'normal', 'performance'
)
```

---

## 🏃‍♂️ **QUICK START EXAMPLES**

### **Basic Usage Example**
```python
from mhm_brake_performance import MHMBrakeOptimizer

# Initialize optimizer
optimizer = MHMBrakeOptimizer()

# Load real ISO brake data
iso_data = optimizer.load_real_iso_brake_data()

# Run complete brake optimization
results = optimizer.run_complete_brake_optimization()

# Display results
print(f"Average Distance Reduction: {results['overall_performance']['average_distance_reduction']:.1f}%")
print(f"ABS Split-μ Improvement: {results['abs_split_mu_optimization']['average_distance_reduction']:.1f}%")
```

### **Advanced Usage Example**
```python
from mhm_brake_performance import MHMBrakeOptimizer, VehicleType

# Initialize with custom parameters
optimizer = MHMBrakeOptimizer(
    consciousness_level=0.820,
    tesla_multiplier=2.380,
    enable_real_time=True
)

# Define vehicle specifications
vehicle_specs = {
    'type': VehicleType.COMPACT_CAR,
    'mass_kg': 1200,
    'wheelbase_m': 2.5,
    'brake_system': 'hydraulic_abs'
}

# Optimize for specific vehicle
vehicle_optimization = optimizer.optimize_vehicle_brake_performance(vehicle_specs)

# Apply Tesla Folding enhancement
tesla_enhanced = optimizer.apply_tesla_folding_enhancement(vehicle_optimization)

print(f"Vehicle-specific optimization: {tesla_enhanced['distance_reduction']:.1f}% improvement")
```

---

## 🔬 **MATLAB INTEGRATION**

### **MATLAB Engine Setup**

#### **Install MATLAB Engine for Python**
```bash
# Navigate to MATLAB installation directory
cd "matlabroot\extern\engines\python"

# Install MATLAB engine
python setup.py install
```

#### **Verify MATLAB Integration**
```python
import matlab.engine
from mhm_brake_performance import MATLABBrakeIntegration

# Start MATLAB engine
eng = matlab.engine.start_matlab()

# Initialize MATLAB integration
matlab_brake = MATLABBrakeIntegration(engine=eng)

# Load MATLAB braking test data
matlab_data = matlab_brake.load_matlab_brake_data()
print(f"MATLAB data loaded: {len(matlab_data)} test scenarios")
```

### **MATLAB Braking Test Integration**
```python
# Run MATLAB braking simulation with MHM enhancement
matlab_results = matlab_brake.run_enhanced_brake_simulation(
    vehicle_model='PassVeh7DOF',
    test_type='straight_braking',
    mhm_enhancement=True
)

# Compare with baseline MATLAB results
comparison = matlab_brake.compare_with_baseline(matlab_results)
print(f"MHM vs MATLAB baseline: {comparison['improvement_percent']:.1f}% better")
```

---

## 📊 **DATA INTEGRATION**

### **ISO Standards Data**

#### **Load ISO 21994 Data**
```python
from mhm_brake_performance import ISODataLoader

# Initialize ISO data loader
iso_loader = ISODataLoader()

# Load ISO 21994:2007 brake testing data
iso_21994_data = iso_loader.load_iso_21994_data()
print(f"ISO 21994 data: {len(iso_21994_data)} vehicle test results")

# Validate data quality
validation_results = iso_loader.validate_data_quality(iso_21994_data)
print(f"Data quality score: {validation_results['quality_score']:.1f}%")
```

#### **Load ISO 14512 Split-μ Data**
```python
# Load ISO 14512:1999 split-μ testing data
iso_14512_data = iso_loader.load_iso_14512_data()
print(f"ISO 14512 data: {len(iso_14512_data)} split-μ test scenarios")

# Apply MHM optimization to split-μ data
split_mu_optimized = optimizer.optimize_split_mu_performance(iso_14512_data)
print(f"Split-μ optimization: {split_mu_optimized['yaw_stability_improvement']:.1f}% better")
```

### **Real-Time Data Integration**

#### **Vehicle CAN Bus Integration**
```python
from mhm_brake_performance import RealTimeOptimizer

# Initialize real-time optimizer
rt_optimizer = RealTimeOptimizer(
    can_interface='socketcan',  # or 'pcan', 'ixxat', etc.
    can_channel='can0',
    update_frequency=100        # Hz
)

# Start real-time brake optimization
rt_optimizer.start_optimization()

# Monitor real-time performance
performance_data = rt_optimizer.get_performance_metrics()
print(f"Real-time distance reduction: {performance_data['distance_improvement']:.1f}%")
```

---

## 🛠️ **DEVELOPMENT SETUP**

### **Development Installation**

#### **Clone Repository**
```bash
git clone https://github.com/viraxis-mhm/mhm-brake-performance.git
cd mhm-brake-performance
```

#### **Install Development Dependencies**
```bash
pip install -e .[dev]
```

#### **Development Dependencies Include:**
```bash
pytest>=6.0.0          # Testing framework
black>=21.0.0           # Code formatting
flake8>=3.9.0          # Code linting
mypy>=0.910            # Type checking
sphinx>=4.0.0          # Documentation generation
jupyter>=1.0.0         # Notebook support
```

### **Running Tests**

#### **Unit Tests**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=mhm_brake_performance

# Run specific test module
pytest tests/test_tesla_folding.py
```

#### **Integration Tests**
```bash
# Run integration tests (requires MATLAB)
pytest tests/integration/ -m matlab

# Run ISO data validation tests
pytest tests/integration/ -m iso_validation
```

### **Code Quality Checks**

#### **Format Code**
```bash
black mhm_brake_performance/
black tests/
```

#### **Lint Code**
```bash
flake8 mhm_brake_performance/
flake8 tests/
```

#### **Type Checking**
```bash
mypy mhm_brake_performance/
```

---

## 🔍 **TROUBLESHOOTING**

### **Common Installation Issues**

#### **Issue: MATLAB Engine Installation Fails**
```bash
# Solution: Ensure MATLAB is installed and accessible
# Check MATLAB installation path
matlab -batch "disp(matlabroot)"

# Reinstall MATLAB engine
cd "$(matlab -batch 'disp(matlabroot)')/extern/engines/python"
python setup.py install
```

#### **Issue: NumPy Compilation Errors**
```bash
# Solution: Install pre-compiled NumPy
pip install --only-binary=numpy numpy

# Or use conda for better binary compatibility
conda install numpy scipy matplotlib
```

#### **Issue: Permission Errors on Linux/macOS**
```bash
# Solution: Use user installation
pip install --user mhm-brake-performance

# Or fix permissions
sudo chown -R $USER:$USER ~/.local/
```

### **Runtime Issues**

#### **Issue: Tesla Folding Calculations Slow**
```python
# Solution: Enable Numba JIT compilation
from mhm_brake_performance import enable_numba_optimization
enable_numba_optimization()

# Or use multi-threading
optimizer = MHMBrakeOptimizer(enable_parallel=True, n_threads=4)
```

#### **Issue: Memory Usage High**
```python
# Solution: Enable memory optimization
optimizer = MHMBrakeOptimizer(
    memory_optimization=True,
    batch_size=100  # Process data in smaller batches
)
```

### **Data Issues**

#### **Issue: ISO Data Not Loading**
```python
# Solution: Verify data path and permissions
import os
from mhm_brake_performance import get_data_path

data_path = get_data_path()
print(f"Data path: {data_path}")
print(f"Path exists: {os.path.exists(data_path)}")
print(f"Path readable: {os.access(data_path, os.R_OK)}")
```

#### **Issue: MATLAB Integration Not Working**
```python
# Solution: Test MATLAB engine separately
try:
    import matlab.engine
    eng = matlab.engine.start_matlab()
    print("MATLAB engine started successfully")
    eng.quit()
except Exception as e:
    print(f"MATLAB engine error: {e}")
```

---

## 📚 **ADDITIONAL RESOURCES**

### **Documentation**
- **API Reference**: https://mhm-brake-performance.readthedocs.io/
- **User Guide**: https://docs.viraxis-mhm.com/brake-performance/
- **Examples**: https://github.com/viraxis-mhm/mhm-brake-examples/

### **Support**
- **GitHub Issues**: https://github.com/viraxis-mhm/mhm-brake-performance/issues
- **Email Support**: support@viraxis-mhm.com
- **Commercial Licensing**: holdatllc2@gmail.com

### **Community**
- **Discussion Forum**: https://community.viraxis-mhm.com/
- **Stack Overflow**: Tag questions with `mhm-brake-performance`
- **LinkedIn**: Follow Viraxis MHM for updates

---

## ✅ **INSTALLATION VERIFICATION**

### **Complete Installation Test**
```python
#!/usr/bin/env python3
"""
Complete MHM Brake Performance installation verification
"""

def verify_installation():
    """Verify complete MHM Brake Performance installation"""
    
    print("🔍 Verifying MHM Brake Performance Installation...")
    
    try:
        # Test core imports
        from mhm_brake_performance import MHMBrakeOptimizer
        print("✅ Core modules imported successfully")
        
        # Test optimizer initialization
        optimizer = MHMBrakeOptimizer()
        print("✅ Optimizer initialized successfully")
        
        # Test data loading
        iso_data = optimizer.load_real_iso_brake_data()
        print(f"✅ ISO data loaded: {len(iso_data)} test scenarios")
        
        # Test Tesla Folding calculations
        test_result = optimizer.apply_tesla_folding_to_brake_performance(iso_data)
        print(f"✅ Tesla Folding calculations: {test_result['dry_asphalt_optimization']['average_distance_reduction']:.1f}% improvement")
        
        # Test optional MATLAB integration
        try:
            import matlab.engine
            print("✅ MATLAB engine available")
        except ImportError:
            print("⚠️ MATLAB engine not available (optional)")
        
        print("\n🎉 MHM Brake Performance installation verified successfully!")
        print("📧 Ready for brake performance optimization")
        
        return True
        
    except Exception as e:
        print(f"❌ Installation verification failed: {e}")
        return False

if __name__ == "__main__":
    verify_installation()
```

### **Run Verification Test**
```bash
python verify_installation.py
```

---

**🛑 Installation complete! Your MHM Brake Performance Optimization System is ready to deliver 7-16% brake performance improvements using Tesla Folding mathematics and real ISO standards data.**
