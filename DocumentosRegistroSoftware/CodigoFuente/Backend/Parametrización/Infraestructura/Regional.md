```
//ENTITY REGIONAL
package com.persona.Backend.Entity.Parameter.Infraestrutura;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Parameter.Ubicacion.Departamento;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "regional")
public class Regional extends BaseEntity {

	@Column(name = "nit", length = 45, nullable = false)
	private String nit;

	@Column(name = "nombre", length = 45, nullable = true)
	private String nombre;

	@Column(name = "acronimo", length = 45, nullable = false)
	private String acronimo;

	@Column(name = "direccion", length = 45, nullable = true)
	private String direccion;

	@Column(name = "telefono", length = 45, nullable = true)
	private String telefono;

	@OneToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "departamento_id", nullable = false, unique = false)
	private Departamento departamentoId;

	public String getNit() {
		return nit;
	}

	public void setNit(String nit) {
		this.nit = nit;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getAcronimo() {
		return acronimo;
	}

	public void setAcronimo(String acronimo) {
		this.acronimo = acronimo;
	}

	public String getDireccion() {
		return direccion;
	}

	public void setDireccion(String direccion) {
		this.direccion = direccion;
	}

	public String getTelefono() {
		return telefono;
	}

	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}

	public Departamento getDepartamentoId() {
		return departamentoId;
	}

	public void setDepartamentoId(Departamento departamentoId) {
		this.departamentoId = departamentoId;
	}

}
//IREPOSITORY REGIONAL
package com.persona.Backend.IRepository.Parameter.Infraestructura;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Regional;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IRegionalRepository extends IBaseRepository<Regional, Long> {

}
//ISERVICE REGIONAL
package com.persona.Backend.IService.Parameter.Infraestructura;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Regional;
import com.persona.Backend.IService.IBaseService;

public interface IRegionalService extends IBaseService<Regional>{

}
//SERVICE REGIONAL
package com.persona.Backend.Service.Parameter.Infraestructura;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Regional;
import com.persona.Backend.IService.Parameter.Infraestructura.IRegionalService;
import com.persona.Backend.Service.BaseService;

@Service
public class RegionalService extends BaseService<Regional> implements IRegionalService {

}
//CONTROLLER REGIONAL
package com.persona.Backend.Controller.Parameter.Infraestructura;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Infraestrutura.Regional;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/parameter/infraestructura/regional")
public class RegionalController extends BaseController<Regional>{

}


```