```
//ENTITY FUNCIONES
package com.persona.Backend.Entity.Operational.GestionPersonal;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ProyectoFormativo;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "funciones")
public class Funciones extends BaseEntity {

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "descripcion", length = 45, nullable = false)
	private String descripcion;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "proyecto_formativo_id", nullable = false, unique = false)
	private ProyectoFormativo proyectoFormativoId;

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public ProyectoFormativo getProyectoFormativoId() {
		return proyectoFormativoId;
	}

	public void setProyectoFormativoId(ProyectoFormativo proyectoFormativoId) {
		this.proyectoFormativoId = proyectoFormativoId;
	}

}
//IREPOSITORY FUNCIONES
package com.persona.Backend.IRepository.Operational.GestionPersonal;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionPersonal.Funciones;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IFuncionesRpository extends IBaseRepository<Funciones, Long>{

}
//ISERVICE FUNCIONES
package com.persona.Backend.IService.Operational.GestionPersonal;

import com.persona.Backend.Entity.Operational.GestionPersonal.Funciones;
import com.persona.Backend.IService.IBaseService;

public interface IFuncionesService extends IBaseService<Funciones>{

}
//SERVICE FUNCIONES
package com.persona.Backend.Service.Operational.GestionPersonal;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionPersonal.Funciones;
import com.persona.Backend.IService.Operational.GestionPersonal.IFuncionesService;
import com.persona.Backend.Service.BaseService;

@Service
public class FuncionesService extends BaseService<Funciones> implements IFuncionesService{

}
//CONTROLLER FUNCIONES
package com.persona.Backend.Controller.Operational.GestionPersonal;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionPersonal.Funciones;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_personal/funciones")
public class FuncionesController extends BaseController<Funciones> {

}

```